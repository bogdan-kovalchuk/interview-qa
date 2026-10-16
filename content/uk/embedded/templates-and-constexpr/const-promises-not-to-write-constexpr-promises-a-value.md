---
id: emb-tmplcx-0007
title: "У чому різниця між `const` і `constexpr`?"
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
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-expr-const
    title: "C++ working draft: Constant expressions ([expr.const])"
    url: https://eel.is/c++draft/expr.const
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
---

## Short answer

**`const` = «не модифікуватиму», але значення може обчислюватися в runtime. `constexpr` = «може бути constant expression».**

Для embedded `constexpr` сильніший: ініціалізатор, який не є константним виразом, дає помилку компіляції.[^cpp-draft-dcl-constexpr] `constexpr`-змінна зі static storage ініціалізується статично, без динамічної ініціалізації під час запуску.[^cpp-draft-expr-const][^cpp-draft-basic-start-static]

Правило: для compile-time констант і таблиць використовуй `constexpr`, а не просто `const`.

## Detailed explanation

`const` означає лише те, що через цю назву об’єкт не змінюють. Він не вимагає, щоб значення було відоме під час компіляції: `const int n = read_adc();` є коректним, і `n` ініціалізується під час виконання. `constexpr` на змінній робить її `const` і додатково вимагає, щоб ініціалізатор був константним виразом: компілятор має обчислити його сам, інакше програма не компілюється.[^cpp-draft-dcl-constexpr]

Стандарт розрізняє статичну й динамічну ініціалізацію. Якщо змінна зі static storage duration є constant-initialized, її значення задається без динамічної ініціалізації під час запуску.[^cpp-draft-expr-const][^cpp-draft-basic-start-static] Усе інше – динамічна ініціалізація, і для нелокальних неінлайнових змінних зі static storage її момент визначає реалізація: вона може виконатися до першого оператора `main`, а може бути відкладена.[^cpp-draft-basic-start-dynamic] Де саме опиниться дані – у Flash (`.rodata`) чи в RAM (`.data`, `.bss`) – стандарт не визначає: це рішення компілятора і скрипта лінкера, тож перевіряйте map file, а не покладайтеся на слово `constexpr`.

Приклад ілюстративний:

```cpp
// Illustrative
constexpr int square(int x) { return x * x; }

const int a = square(3);          // constant expression: constant initialization, a == 9
static_assert(a == 9, "a is usable in constant expressions");

int read_adc();                   // defined elsewhere; value known only at run time
const int b = read_adc();         // const only: dynamic initialization
// constexpr int c = read_adc();  // error: initializer is not a constant expression
```

`const` для цілого типу з константним ініціалізатором часто теж працює як константа, але для інших типів ні: `const float f = 1.0f;` не можна використати в `static_assert`, а `constexpr float` можна. Причина в тому, що потенційно сталими є лише `constexpr`-змінні, посилання та non-volatile `const` цілого або перелічуваного типу.[^cpp-draft-expr-const] Тому правило практичне: якщо значення має бути відоме компілятору (`static_assert`, розмір буфера, таблиця), пишіть `constexpr`.

**Типові помилки:**

- Вважати, що `const` означає compile-time константу: `const int n = read_adc();` компілюється, але `n` не є константою.
- Очікувати, що `const float` можна використати в `static_assert`: для таких типів потрібен `constexpr`.[^cpp-draft-expr-const]
- Вважати, що `constexpr` сам по собі кладе дані у Flash: розміщення визначають компілятор і лінкер.
