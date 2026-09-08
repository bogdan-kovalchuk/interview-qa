---
id: cpp-ptrref-0001
title: "unique_ptr чи shared_ptr: як обрати між ними?"
description: "Ексклюзивне володіння – типовий вибір; спільне володіння додає облік спільного часу життя."
track: cpp
section: pointers-and-references
level: middle
type: comparison
tags: [smart-pointers, ownership, raii, lifetime]
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  en: 3
applies_to:
  - product: ISO C++
    version: "C++20"
anki:
  export: true
sources:
  - source_id: cpp-draft-smartptr
    title: "C++ working draft: smart pointers ([smartptr])"
    url: https://eel.is/c++draft/smartptr
    accessed: 2026-09-04
    kind: spec
    version: "C++20"
    applicability: семантика володіння і збереження deleter; стандарт задає поведінку, а не розмір об'єкта
  - source_id: cppreference-unique-ptr
    title: "cppreference: std::unique_ptr"
    url: https://en.cppreference.com/w/cpp/memory/unique_ptr
    accessed: 2026-09-03
    kind: community
    version: "C++20"
    applicability: "Move-only семантика, зберігання deleter і типові характеристики реалізацій до C++20; розмір об'єкта не гарантовано."
  - source_id: cppreference-shared-ptr
    title: "cppreference: std::shared_ptr"
    url: https://en.cppreference.com/w/cpp/memory/shared_ptr
    accessed: 2026-09-03
    kind: community
    version: "C++20"
    applicability: "Спільне володіння, реалізації control block, правила потокобезпеки й типова поведінка алокації make_shared до C++20."
---

## Short answer

**Бери `unique_ptr`, доки в часу життя справді не з'явиться кілька незалежних власників.** Він є
move-only і зберігає вказівник разом із deleter; стандарт не гарантує розмір сирого вказівника чи
нульову runtime-вартість.[^cpp-draft-smartptr] `shared_ptr` ділить володіння через облік, який
зазвичай міститься в control block. Копії можуть потребувати синхронізації, а сам pointee не отримує
потокобезпеки. Об'єкт знищується, коли його відпускає останній власник; ownership cycles потребують
`weak_ptr`.[^cppreference-shared-ptr]

## Detailed explanation

Обидва типи виражають володіння, і різниця в тому, скільки власників дозволено.

`unique_ptr` стверджує, що власник у кожен момент рівно один. Його не можна копіювати, лише
переміщувати, і саме це обмеження робить володіння читабельним із сигнатури: функція, що приймає
`unique_ptr<T>` за значенням, забирає володіння, а та, що приймає `T*` або `T&`, позичає. З default
deleter він часто представлений одним вказівником, а знищення прямо викликає збережений deleter.
Стандарт не гарантує ані layout, ані нульових overhead.[^cpp-draft-smartptr] Stateful deleter,
наприклад лямбда із захопленням або вказівник на функцію, зберігається у smart pointer і може додати
розмір або ціну виклику.

`shared_ptr` стверджує, що володіння спільне і прибирає останній власник. Для цього потрібен control
block, де реалізації зазвичай тримають ownership counts і deleter. Ці лічильники зазвичай
використовують атомарні операції. Стандарт гарантує, що різні об'єкти `shared_ptr` зі спільним
володінням можна використовувати конкурентно без data race в ownership machinery, але сам pointee
не отримує захисту: два потоки, що пишуть у нього, все одно можуть мати data race.[^cpp-draft-smartptr]
Реалізації зазвичай дозволяють `make_shared` виділити control block і об'єкт разом; це може
зекономити алокацію, але залишити комбіноване storage живим, поки існує `weak_ptr`.[^cppreference-shared-ptr]

```cpp
struct Node {
    std::unique_ptr<Node> next;      // exclusive: the list owns its tail
    std::shared_ptr<Config> config;  // shared: many nodes read one config
    std::weak_ptr<Node> parent;      // observing: breaks the ownership cycle
};
```

Дорога помилка – не одне оновлення лічильника, а втрачена відповідь на питання «хто це видаляє і
коли». Граф власників-`shared_ptr` знищує об'єкт тоді й там, де його відпустив останній власник, а це
може бути не потік творця. Ownership cycle не звільняє нічого взагалі.

## Comparison

| | `unique_ptr` | `shared_ptr` |
|---|---|---|
| Власників | рівно один | будь-яка кількість |
| Копіюється | ні, лише move | так |
| Типове представлення | часто один вказівник | часто два вказівники плюс control block |
| Додаткова алокація | не потрібна для володіння | control block; часто об'єднаний через `make_shared` |
| Ціна копіювання | move вказівника й deleter | облік спільного володіння, часто синхронізований |
| Точка знищення | детермінована, на виході зі scope | там, де відпустив останній власник |
| Цикли | неможливі | можливі, розриваються `weak_ptr` |
| Потокобезпека | не потрібна | лише лічильник, ніколи об'єкт |

## When to choose which

Обирай `unique_ptr` для поля, яким володіє клас, для значення, що повертає фабрика, для pimpl і для
будь-якої передачі володіння через межу API. Це типовий вибір, бо він документує час життя й уникає
обліку спільного володіння.

Обирай `shared_ptr`, коли кількість власників справді невідома під час компіляції: кеш, відданий
кільком підсистемам; вузол графа, що переживає обхід, який його знайшов; об'єкт, захоплений
асинхронним callback, який може завершитись після зникнення свого творця. Передавай його за значенням
лише тоді, коли викликана сторона його зберігає; інакше передавай посилання або сирий вказівник, бо
позичання не потребує володіння.

Використовуй `weak_ptr` там, де спостерігач не має тримати об'єкт живим, і перевіряй його через
блокування, а не через тест на expiry, бо між цими двома викликами об'єкт може померти.

## Evaluation guide

### Expected signals

- Називає вирішальним питанням ексклюзивне проти спільного володіння, а не продуктивність.
- Знає, що `unique_ptr` є move-only, і відрізняє типову zero-overhead реалізацію від гарантії
  стандарту.
- Знає, що shared ownership потребує обліку, часто з атомарними лічильниками, і що це не захищає
  pointee.
- Сам, без підказки, згадує цикли і `weak_ptr`.

### Red flags

- «`shared_ptr` безпечніший, тож використовуй його всюди».
- Вважає, що `shared_ptr` робить потокобезпечним сам об'єкт.
- Передає `shared_ptr` за значенням у функції, які лише читають об'єкт, і не може сказати, чого це
  коштує.

### Level-up follow-up

Спитати, що змінюється, якщо останнє посилання відпускається не в тому потоці, який створив об'єкт,
і як кандидат тримав би знищення в обраному потоці.

## Sources

<!-- generated from frontmatter -->
