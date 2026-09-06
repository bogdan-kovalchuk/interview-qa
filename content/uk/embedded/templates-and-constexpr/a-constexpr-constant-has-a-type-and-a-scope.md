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
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

```cpp
constexpr int MAX_SENSORS = 16;
// vs  #define MAX_SENSORS 16
```

**Має тип і scope – типобезпечна, на відміну від текстової заміни.**

`constexpr`-змінна ініціалізується на етапі компіляції, видима дебагеру, поважає namespace і бере участь у перевірці типів. `#define` – лише текст без типу.

Правило: цілочисельні compile-time константи в C++ – `constexpr`, не `#define`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
