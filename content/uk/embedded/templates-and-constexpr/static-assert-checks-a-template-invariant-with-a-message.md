---
id: emb-tmplcx-0027
title: "Як `static_assert` використовують із шаблонами?"
description: "Compile-time перевірка інваріантів типу/розміру з понятним повідомленням."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
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

**Compile-time перевірка інваріантів типу/розміру з понятним повідомленням.**

Напр. у дефолтній гілці `if constexpr`: `static_assert(always_false<P>, "Unsupported platform")` ловить непідтримуваний тип ще на компіляції. Також `static_assert(N > 0, "...")` валідовує NTTP.

Правило: `static_assert` – головний інструмент, щоб перетворити невірне використання шаблону на зрозумілу помилку.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
