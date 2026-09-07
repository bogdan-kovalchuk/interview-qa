---
id: emb-cppstl-0031
title: "Trap: why is a raw C array in a C++ signature a bad signal in an interview?"
description: "A raw C array decays to a pointer losing its size and signals ignorance of modern C++ practices."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
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

<span class="warn">It decays to a pointer (losing the size) and shows ignorance of modern practices.</span>

`void f(int arr[])` actually takes `int*`; `sizeof` inside gives the pointer size. `std::array`/`std::span` preserve the size and are safer.

Protection: in C++ pass `std::array&`, `std::span` or (container + size), not a bare `T[]`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
