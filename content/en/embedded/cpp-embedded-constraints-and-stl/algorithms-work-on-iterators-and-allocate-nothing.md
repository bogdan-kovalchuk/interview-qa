---
id: emb-cppstl-0014
title: "Why are `<algorithm>` and `<numeric>` safe even without a heap?"
description: "They operate on iterators rather than containers and never allocate memory themselves."
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

**They operate on iterators rather than containers – they never allocate memory themselves.**

`std::sort`, `std::find`, `std::copy`, `std::accumulate` work on a `[begin, end)` range, so they can be applied to `std::array` or even a C array.

Rule: STL algorithms are header-only and heap-free; it is the heap containers that are dangerous, not the algorithms.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
