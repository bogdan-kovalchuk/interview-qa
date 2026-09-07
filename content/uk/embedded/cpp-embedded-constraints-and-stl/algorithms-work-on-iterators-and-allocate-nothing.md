---
id: emb-cppstl-0014
title: "Чому `<algorithm>` і `<numeric>` безпечні навіть без heap?"
description: "Вони працюють на ітераторах, а не на контейнерах – не алокують пам'ять самі."
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

**Вони працюють на ітераторах, а не на контейнерах – не алокують пам'ять самі.**

`std::sort`, `std::find`, `std::copy`, `std::accumulate` оперують діапазоном `[begin, end)`, тож їх можна застосовувати до `std::array` чи навіть C-масиву.

Правило: алгоритми STL – header-only й heap-free; небезпечні саме heap-контейнери, а не алгоритми.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
