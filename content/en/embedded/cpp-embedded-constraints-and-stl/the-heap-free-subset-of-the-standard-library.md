---
id: emb-cppstl-0009
title: "Which STL components are safe (heap-free) for embedded?"
description: "std::array, std::optional, std::stringview, std::bitset, std::tuple, std::variant are heap-free"
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

**`std::array`, `std::optional`, `std::string_view`, `std::bitset`, `std::tuple`/`std::pair`, `std::variant`, ``, ``.**

All of them have fixed size or work on iterators without allocation. `std::sort`, `std::find`, `std::accumulate` are header-only, no heap.

Rule: STL (standard template library) is not forbidden entirely – its heap-free subset is safe.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
