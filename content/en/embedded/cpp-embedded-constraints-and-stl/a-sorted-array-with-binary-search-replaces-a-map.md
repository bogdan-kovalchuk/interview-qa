---
id: emb-cppstl-0028
title: "How do you replace `std::map` without a heap?"
description: "A sorted std::array of pairs with binary search via std::lowerbound replaces std::map without any allocation."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
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

**A sorted `std::array` of pairs + binary search (`std::lower_bound`).**

`std::map` allocates nodes on the heap for every insertion. If the key set is known at compile time, a `constexpr` sorted array gives O(log n) lookup without any allocation.

Rule: static lookup tables – sorted `array` + binary search instead of `map`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
