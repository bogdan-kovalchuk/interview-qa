---
id: emb-cppstl-0011
title: "How is `std::array` better than a raw C array?"
description: "Zero-overhead wrapper over a C array with .size(), .at() and compatibility with algorithms"
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

**Zero-overhead wrapper over a C array with `.size()`, `.at()` (with bounds checking) and compatibility with ``.**

It does not decay to a pointer when passed, knows its size and works with `std::sort`/`std::find`. Size and layout are identical to a C array.

Rule: in C++ embedded `std::array` fully replaces `T[]` as the default container.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
