---
id: emb-cppstl-0009
title: "Які STL-компоненти безпечні (heap-free) для embedded?"
description: "std::array, std::optional, std::string_view, std::bitset, std::tuple/std::pair, std::variant, , ."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**`std::array`, `std::optional`, `std::string_view`, `std::bitset`, `std::tuple`/`std::pair`, `std::variant`, ``, ``.**

Усі вони мають фіксований розмір або працюють на ітераторах без алокації. `std::sort`, `std::find`, `std::accumulate` – header-only, без heap.

Правило: STL (standard template library) не заборонена цілком – безпечна її heap-free підмножина.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
