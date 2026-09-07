---
id: emb-cppstl-0029
title: "Чому `enum class` кращий за звичайний `enum` для статусів?"
description: "Scoped і strongly-typed: не конвертується неявно в int і не засмічує namespace."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Scoped і strongly-typed: не конвертується неявно в `int` і не засмічує namespace.**

`Status::Ok` не сплутати з іншим enum'ом, і `if (status)` не скомпілюється випадково. Це ловить цілий клас помилок порівняння/перетворення.

Правило: для кодів помилок і станів використовуй `enum class`, а не голий `enum`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
