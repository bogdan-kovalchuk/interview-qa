---
id: emb-tmplcx-0008
title: "Чому `constexpr`-змінна краща за `#define`-константу?"
description: "Має тип і scope – типобезпечна, на відміну від текстової заміни."
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
  - source_id: cpp-draft-cpp-replace
    title: "C++ working draft: Replacement of macros ([cpp.replace])"
    url: https://eel.is/c++draft/cpp.replace
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає object-like макрос: його ім’я замінюється списком заміни з токенів препроцесора. Це текстова підстановка без типу; конкретний препроцесор не описано."
  - source_id: cpp-draft-lex-phases
    title: "C++ working draft: Phases of translation ([lex.phases])"
    url: https://eel.is/c++draft/lex.phases
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що на фазі 4 трансляції розгортаються виклики макросів, а на фазі 7 токени синтаксично й семантично аналізуються як translation unit. Конкретний препроцесор не описано."
  - source_id: cpp-draft-cpp-scope
    title: "C++ working draft: Scope of macro definitions ([cpp.scope])"
    url: https://eel.is/c++draft/cpp.scope
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що визначення макроса діє незалежно від блочної структури, до #undef або кінця translation unit, і не має значення після фази 4 трансляції."
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що constexpr на об’єкті робить його const і вимагає, щоб ініціалізатор був constant-initializable; інакше програма некоректна."
  - source_id: cpp-draft-dcl-init-list
    title: "C++ working draft: List-initialization ([dcl.init.list])"
    url: https://eel.is/c++draft/dcl.init.list
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає звуження при list-initialization: перетворення цілого типу, яке не може представити всі його значення, є звуженням, якщо джерело не константний вираз, чия величина після перетворення вміщується в тип. Тому 300 у uint8_t – звуження."
---

## Question code

```cpp
constexpr int MAX_SENSORS = 16;
// vs  #define MAX_SENSORS 16
```

## Short answer

**Має тип і scope – типобезпечна, на відміну від текстової заміни.**

`constexpr`-змінна має тип і звичайну область видимості, а її ініціалізатор мусить бути константним виразом.[^iso-cpp-n4861][^cpp-draft-dcl-constexpr] `#define` – текстова підстановка препроцесора: макрос не має типу й scope, а заміна відбувається на фазі 4 трансляції.[^cpp-draft-cpp-replace][^cpp-draft-lex-phases][^cpp-draft-cpp-scope]

Правило: цілі compile-time константи в C++ – `constexpr`, не `#define`; `#define` лишається для умовної компіляції.

## Detailed explanation

Макрос обробляється до аналізу мови. На фазі 4 трансляції препроцесор замінює його ім’я списком токенів, а лише на фазі 7 код аналізується як C++.[^cpp-draft-lex-phases][^cpp-draft-cpp-replace] Тому в `#define MAX_SENSORS 16` немає об’єкта: компілятор бачить лише `16`. Це видно в `sizeof`: `sizeof(LIMIT_MACRO)` дорівнює `sizeof(int)`, бо це `sizeof(300)`, тоді як `sizeof(kRetries)` дорівнює 1, бо `kRetries` має тип `uint8_t`.

`constexpr` – це звичайна змінна з типом, яку перевіряє компілятор. `constexpr std::uint8_t kRetries{5};` має тип `uint8_t`, а `constexpr std::uint8_t kLimit{300};` не компілюється: список ініціалізації відхиляє звуження, бо 300 не вміщується в `uint8_t`.[^cpp-draft-dcl-init-list] Тип `constexpr` перевіряється один раз, при оголошенні; макрос не має оголошеного типу, тож звуження перевіряється лише там, де його використано з типом (наприклад, `std::uint8_t x{LIMIT_MACRO};` дає ту саму помилку). Щодо області видимості макрос діє від свого визначення до `#undef` або кінця translation unit, незалежно від блоків.[^cpp-draft-cpp-scope] Тому `uart::kBaudDiv` і `spi::kBaudDiv` співіснують в одному файлі; макрос такого розділення не має, бо його ім’я діє на весь translation unit.

Приклад (ілюстративний, компілюється):

```cpp
#include <cstdint>

namespace uart { constexpr std::uint32_t kBaudDiv = 0x34; }  // scope: uart::
namespace spi  { constexpr std::uint32_t kBaudDiv = 0x08; }  // same name, other scope

constexpr std::uint8_t kRetries{5};          // typed; the compiler checks it
// constexpr std::uint8_t kLimit{300};       // error: narrowing, 300 does not fit uint8_t

#define LIMIT_MACRO 300                      // text only: no type, no scope
static_assert(sizeof(LIMIT_MACRO) == sizeof(int), "the macro expands to the int literal 300");
static_assert(sizeof(kRetries) == 1, "constexpr std::uint8_t is one byte");
```

Не всі `#define` варто замінювати. `#if`, `#ifdef` і include guard вирішують, які рядки взагалі потраплять до компіляції, тож `constexpr` їх не замінює. Замінювати варто саме значення-константи, як `16` чи `0x34`.

**Типові помилки:**

- Вважати `#define` безпечним, бо це «просто число»: без типу `sizeof` і перевірка звуження в місці використання поводяться інакше.
- Лишати `#define` для констант окремого модуля: ім’я макроса діє в усьому translation unit, а `constexpr` у namespace видно лише через ім’я простору.
- Вважати, що `constexpr` замінює `#ifdef`: вибір драйвера за платформою лишається препроцесорним.

## Sources

<!-- generated from frontmatter -->
