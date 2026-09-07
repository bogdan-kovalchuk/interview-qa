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
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**`const` = «не модифікуватиму», але значення може обчислюватися в runtime. `constexpr` = «може бути constant expression».**

Для embedded `constexpr` сильніший: він змушує ініціалізацію бути придатною для compile-time обчислення і для об'єктів зі static storage зазвичай веде до готових даних у Flash/`.rodata`, а не startup-розрахунку в RAM.

Правило: для compile-time констант/таблиць використовуй `constexpr`, а не просто `const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
