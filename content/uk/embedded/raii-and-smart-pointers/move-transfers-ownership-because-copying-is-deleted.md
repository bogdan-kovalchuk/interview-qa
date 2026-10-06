---
id: emb-raii-0009
title: "Як передати володіння ресурсом через `unique_ptr`?"
description: "Через std::move() – копіювання заборонене, передача явна."
track: embedded
section: raii-and-smart-pointers
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
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що unique_ptr має strict ownership: його можна move-конструювати й move-присвоювати, але не копіювати. Про використання в конкретних системах нічого не каже."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає deleted copy-операції; move-конструктор (після нього `get()` джерела дорівнює `nullptr`, deleter переноситься); move-присвоєння (`reset(u.release())`, потім присвоєння deleter); precondition `get() != nullptr` для `operator*` і `operator->`. Не описує поведінку конкретної платформи."
  - source_id: cpp-draft-forward
    title: "C++ working draft: forward/move ([forward])"
    url: https://eel.is/c++draft/forward
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає `std::move(t)` як `static_cast<remove_reference_t<T>&&>(t)`, тобто лише cast до rvalue; сам перенос визначають move-конструктор чи move-присвоєння типу."
  - source_id: cppcg-r32-sink-unique-ptr
    title: "C++ Core Guidelines: R.32 – Take a unique_ptr<widget> parameter to express that a function assumes ownership of a widget"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r32-take-a-unique_ptrwidget-parameter-to-express-that-a-function-assumes-ownership-of-a-widget
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: параметр `unique_ptr<widget>` за значенням документує й закріплює передачу власності функції. Це рекомендація, а не вимога мови."
  - source_id: cppcg-f48-dont-return-move-local
    title: "C++ Core Guidelines: F.48 – Don’t return std::move(local)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f48-dont-return-stdmovelocal
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: повернення локальної змінної і так її неявно переміщує, а явний `std::move` перешкоджає RVO, тобто є pessimization. Це рекомендація, а не вимога мови."
---

## Short answer

**Через `std::move()` – копіювання заборонене, передача явна.** `auto b = std::move(a);` переносить власність: `a` стає порожнім (`a.get() == nullptr`), `b` тепер відповідає за звільнення.[^cpp-draft-unique-ptr-single] Сам `std::move` лише приводить вираз до rvalue, а перенос виконує move-конструктор чи move-присвоєння `unique_ptr`.[^cpp-draft-forward] Правило: `unique_ptr` – move-only; явний `std::move` документує, хто тепер власник, а для значення, що повертається з функції, `std::move` не потрібен.[^cppcg-f48-dont-return-move-local]

## Detailed explanation

`unique_ptr` реалізує strict ownership: об’єкт, яким він володіє, має рівно одного власника. Тому його можна move-конструювати й move-присвоювати, але не копіювати, а copy-конструктор і copy-присвоєння явно deleted.[^cpp-draft-unique-ptr-general] Звідси єдиний спосіб передати володіння: перенести його. Якби копіювання було дозволене, два об’єкти після цього вважали б себе власниками й обидва викликали б deleter, тобто ресурс звільнявся б двічі.

Сам `std::move(a)` нічого не переносить: це `static_cast<T&&>(a)`, який лише дозволяє компілятору вибрати перевантаження, що приймає rvalue.[^cpp-draft-forward] Перенос виконує move-конструктор `unique_ptr`: новий об’єкт отримує збережений вказівник і deleter, а `a.get()` після цього дорівнює `nullptr`.[^cpp-draft-unique-ptr-single] Move-присвоєння `b = std::move(a)` діє як `reset(a.release())` з наступним присвоєнням deleter, тож `b` спершу звільняє те, чим володів раніше, а потім приймає ресурс з `a`.[^cpp-draft-unique-ptr-single]

У межах API це дає читабельне правило. Функція, що приймає власність, бере `unique_ptr<T>` за значенням, і це видно в сигнатурі.[^cppcg-r32-sink-unique-ptr] У точці виклику `std::move(p)` показує, що `p` більше не власник. Фабрика повертає `unique_ptr` за значенням без `std::move`: локальна змінна переноситься неявно, а явний `std::move` лише блокує RVO.[^cppcg-f48-dont-return-move-local] У вбудованих системах так зручно передавати, наприклад, буфер із пулу від функції, що його заповнила, до функції, що його відправляє: custom deleter повертає буфер у пул, а власність у кожен момент належить одному місцю.

```cpp
// Ілюстративний приклад; Frame – довільний тип.
std::unique_ptr<Frame> make_frame();       // повертає власність
void send(std::unique_ptr<Frame> f);       // sink: бере власність

void pipeline() {
  auto a = make_frame();                   // без std::move
  auto b = std::move(a);                   // a.get() == nullptr
  send(std::move(b));                      // b порожній, Frame звільнить send()
}
```

**Типові помилки:**

- Використовувати об’єкт після move: розіменування порожнього `unique_ptr` порушує precondition `get() != nullptr`, а це undefined behavior.[^cpp-draft-unique-ptr-single] Перевірити стан можна через `if (a)`.
- Вважати, що `std::move` сам переносить власність: це лише cast, а без move-конструктора чи присвоєння `unique_ptr` нічого не змінюється.[^cpp-draft-forward]
- Писати `return std::move(local);`: це pessimization, яка блокує RVO.[^cppcg-f48-dont-return-move-local]
- Передавати `unique_ptr` за значенням у функцію, яка лише користується ресурсом: для цього досить `T*` чи `T&`, а `unique_ptr` у сигнатурі означає передачу власності.

## Sources

<!-- generated from frontmatter -->
