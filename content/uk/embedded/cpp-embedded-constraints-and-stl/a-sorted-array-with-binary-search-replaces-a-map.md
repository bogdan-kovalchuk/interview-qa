---
id: emb-cppstl-0028
title: "Як замінити `std::map` без heap?"
description: "Відсортований std::array пар + binary search (std::lower_bound)."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Відсортований `std::array` пар + binary search (`std::lower_bound`).**

`std::map` алокує вузли в купі на кожну вставку. Якщо набір ключів відомий на етапі компіляції, `constexpr` відсортований масив дає O(log n) пошук без жодної алокації.

Правило: статичні lookup-таблиці – sorted `array` + binary search замість `map`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
