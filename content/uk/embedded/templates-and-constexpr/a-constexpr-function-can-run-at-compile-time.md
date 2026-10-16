---
id: emb-tmplcx-0005
title: "Що таке constexpr-функція?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
---

## Short answer

**Функція, яку можна викликати в константному виразі; у такому контексті вона обчислюється під час компіляції, в інших місцях – як звичайний виклик.**

Виклик constexpr-функції дає той самий результат, що й виклик звичайної функції, але може стояти в константному виразі.[^cpp-draft-dcl-constexpr] Constexpr-змінна мусить бути constant-initializable, тож вона не потребує динамічної ініціалізації під час запуску.[^cpp-draft-basic-start-static]

Правило: `constexpr` не гарантує обчислення під час компіляції для кожного виклику; потрібен константний контекст, наприклад `static_assert`.

## Detailed explanation

`constexpr` перед функцією дозволяє використати її в constant expression, тобто там, де компілятор має отримати значення під час компіляції: розмір масиву, аргумент шаблону, ініціалізатор constexpr-змінної або `static_assert`. За стандартом виклик constexpr-функції дає той самий результат, що й виклик еквівалентної не-constexpr функції в тому самому контексті; відмінності – зокрема те, що виклик може бути константним виразом, а copy elision у константному виразі не виконується.[^cpp-draft-dcl-constexpr]

Аргументи, відомі тільки під час роботи, роблять виклик звичайним викликом у runtime. Тому `constexpr` не означає «завжди обчислюється компілятором». Щоб переконатися, що значення справді обчислене під час збирання, використовують `static_assert` або constexpr-змінну: якщо аргумент не константа, збирання зупиняється з помилкою. Ілюстративний приклад:

```cpp
#include <cstdint>

constexpr std::uint32_t square(std::uint32_t x) { return x * x; }

constexpr std::uint32_t kLimit = square(16);     // compile-time: constant expression
static_assert(kLimit == 256, "computed at compile time");

std::uint32_t runtime_value(std::uint32_t x) {
  return square(x);                              // ordinary call at run time
}
```

Для таблиць це важливо: constexpr-змінна з static storage має бути constant-initializable, тож її значення формується під час збирання, а не в коді запуску.[^cpp-draft-dcl-constexpr][^cpp-draft-basic-start-static] Де саме розмістити таке значення (у read-only даних чи в RAM), вирішують компілятор і скрипт лінкера цільової плати.

**Типові помилки:**

- Вважати, що кожен виклик constexpr-функції виконується під час компіляції: з аргументом, відомим лише під час роботи, це звичайний виклик.
- Очікувати від `constexpr` прискорення runtime-коду: ключове слово описує можливість константного обчислення, а не гарантію швидкості.
- Не перевіряти результат через `static_assert` чи constexpr-змінну: без них незрозуміло, чи обчислення справді відбулося під час компіляції.
