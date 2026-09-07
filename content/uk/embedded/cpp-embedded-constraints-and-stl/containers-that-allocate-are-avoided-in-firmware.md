---
id: emb-cppstl-0010
title: "Яких STL-компонентів уникають у embedded і чому?"
description: "std::vector, std::string, std::map/unordered_map, std::shared_ptr, <iostream> – вони часто тягнуть heap або важку runtime-інфраструктуру."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">`std::vector`, `std::string`, `std::map`/`unordered_map`, `std::shared_ptr`, `<iostream>` – вони часто тягнуть heap або важку runtime-інфраструктуру.</span>

`vector`/`string` зазвичай алокують динамічний масив; `map` – вузли в купі; `shared_ptr` – control block; `<iostream>` може тягнути locale, буфери й десятки КБ Flash залежно від бібліотеки.

Правило: заміняй на `std::array`, `std::string_view`/`char[]`, відсортований `array` + binary search.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
