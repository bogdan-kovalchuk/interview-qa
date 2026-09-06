---
id: emb-tmplcx-0029
title: "Як constexpr дає compile-time bounds checking?"
description: "Коли розмір – NTTP, індекси/межі можна перевірити static_assert-ом на етапі компіляції."
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

**Коли розмір – NTTP, індекси/межі можна перевірити `static_assert`-ом на етапі компіляції.**

Напр. `get<I>()` з `static_assert(I < N, "out of range")` зробить вихід за межі compile error, а не runtime-багом.

Правило: переноси перевірку меж у compile time скрізь, де індекс/розмір відомі статично.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
