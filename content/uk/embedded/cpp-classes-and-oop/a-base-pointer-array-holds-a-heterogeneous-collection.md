---
id: emb-cppoop-0019
title: "Навіщо потрібен поліморфізм через `Sensor*` масив?"
description: "Гетерогенна колекція: різні конкретні типи за спільним інтерфейсом в одному масиві/контейнері."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що вказівник на похідний клас можна перетворити на вказівник на його базовий клас; саме це дозволяє тримати вказівники на різні похідні типи як Sensor*. Про virtual dispatch не йдеться."
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що виклик virtual-функції виконує її final overrider у dynamic type об’єкта; сам механізм (vptr/vtable) стандарт не задає."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає клас із virtual-функцією як polymorphic і пояснює (note), що трактування virtual-виклику залежить від dynamic type об’єкта, а не-virtual – лише від static type вказівника чи посилання; vtable не згадує."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Описує vtable як таблицю для dispatch virtual-функцій і vptr в об’єкті dynamic class. Це ABI, а не стандарт мови: ABI конкретного тулчейну може відрізнятися."
---

## Short answer

**Гетерогенна колекція: різні конкретні типи за спільним інтерфейсом в одному масиві/контейнері.**

```cpp
Sensor* arr[] = { &temp, &pressure, &humid };
for (auto s : arr) s->read();
```

Виклик через вказівник на base виконує final overrider за dynamic type об’єкта,[^cpp-draft-expr-call] а типово це реалізовано через vptr і vtable.[^itanium-cxx-abi]

Правило: коли треба тримати різні типи разом і викликати їх однаково, virtual – класичний варіант, хоча й не єдиний (є ще, наприклад, tagged union чи таблиця function pointers).

## Detailed explanation

Задача така: є кілька різних датчиків (`Temp`, `Pressure`, `Humidity`), а код опитування має працювати з усіма однаково й не знати, який тип стоїть у кожному елементі. Спільний інтерфейс – базовий клас `Sensor` з `virtual`-методом `read()`. Масив `Sensor*` – це масив вказівників, тож у ньому поруч лежать адреси об’єктів різних похідних класів: вказівник на похідний клас можна перетворити на вказівник на його base.[^cpp-draft-conv-ptr] Новий датчик – це новий клас і новий елемент масиву; цикл опитування не змінюється.

Який саме `read()` виконається, вирішується під час виконання: для virtual-функції викликається final overrider у dynamic type об’єкта.[^cpp-draft-expr-call] Для не-virtual методу було б навпаки: результат залежав би лише від типу вказівника чи посилання, тобто завжди викликався б `Sensor::read`.[^cpp-draft-class-virtual] Реалізація через vptr в кожному об’єкті та vtable на клас є типовою, але це справа ABI, а не стандарту мови.[^itanium-cxx-abi]

Умови й межі. Колекція має тримати вказівники чи посилання: масив самих `Sensor` не вміщає різні похідні об’єкти. Об’єкти мають жити довше за масив; на мікроконтролері їх зазвичай роблять статичними, без heap. Якщо колекція володіє об’єктами й видаляє їх через вказівник на base, потрібен virtual destructor (див. `qid:emb-cppoop-0017`). Кожен поліморфний об’єкт несе vptr, а кожен клас – vtable (див. `qid:emb-cppoop-0013`). Якщо ж набір типів відомий на етапі компіляції, а вартість dispatch важлива, розглядай CRTP чи шаблони (див. `qid:emb-cppoop-0021`).

Ілюстративний приклад:

```cpp
#include <cstdint>

struct Sensor {
    virtual std::int16_t read() = 0;
    virtual ~Sensor() = default;
};
struct Temp final : Sensor { std::int16_t read() override { return 25; } };
struct Pressure final : Sensor { std::int16_t read() override { return 1013; } };

Temp temp;
Pressure pressure;                           // статичні об’єкти, без heap
Sensor* const sensors[] = { &temp, &pressure };

int sum() {
    int total = 0;
    for (Sensor* s : sensors) total += s->read();   // final overrider за dynamic type
    return total;
}
```

**Типові помилки:**

- Робити масив `Sensor` за значенням: для абстрактного base це не компілюється, а для конкретного похідні дані «відрізаються» (slicing) і поліморфізму немає.
- Забути `virtual` у методі base: тоді результат виклику визначає static type вказівника, і виконується `Sensor::read`.[^cpp-draft-class-virtual]
- Залишити в масиві вказівник на об’єкт, що вже вийшов зі scope.
- Вважати virtual єдиним способом зібрати різні типи: для малого фіксованого набору простіші tagged union чи таблиця function pointers.

## Sources

<!-- generated from frontmatter -->
