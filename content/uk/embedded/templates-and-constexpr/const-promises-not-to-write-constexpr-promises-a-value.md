---
id: emb-tmplcx-0007
title: "У чому різниця між `const` і `constexpr`?"
description: "const = «не модифікуватиму», але значення може обчислюватися в runtime."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що constexpr на об’єкті робить його const і вимагає, щоб ініціалізатор був constant-initializable; інакше програма некоректна. Про розміщення даних у Flash чи RAM не йдеться."
  - source_id: cpp-draft-expr-const
    title: "C++ working draft: Constant expressions ([expr.const])"
    url: https://eel.is/c++draft/expr.const
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає constant-initializable змінні: такі змінні constant-initialized, якщо мають ініціалізатор. Потенційно сталими є constexpr-змінні, посилання та non-volatile const цілого або перелічуваного типу, тож const float не є константним виразом. Про розміщення в пам’яті не йдеться."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає constant initialization для об’єктів зі static storage duration і каже, що вся інша ініціалізація є динамічною. Не говорить, чи дані лежать у Flash або RAM."
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що для нелокальної змінної зі static storage, яка ініціалізується динамічно, реалізація визначає, чи ініціалізація виконується до першого оператора main, чи відкладається."
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

## Sources

<!-- generated from frontmatter -->
