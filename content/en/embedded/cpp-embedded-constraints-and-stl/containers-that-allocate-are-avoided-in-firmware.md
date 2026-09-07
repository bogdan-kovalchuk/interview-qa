---
id: emb-cppstl-0010
title: "Which STL components are avoided in embedded and why?"
description: "std::vector, std::string, std::map, std::sharedptr and iostream pull in heap or heavy runtime"
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

<span class="warn">`std::vector`, `std::string`, `std::map`/`unordered_map`, `std::shared_ptr`, `<iostream>` – they often pull in the heap or heavy runtime infrastructure.</span>

`vector`/`string` typically allocate a dynamic array; `map` uses nodes on the heap; `shared_ptr` has a control block; `<iostream>` can pull in locales, buffers and tens of KB of Flash depending on the library.

Rule: replace with `std::array`, `std::string_view`/`char[]`, a sorted `array` + binary search.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
