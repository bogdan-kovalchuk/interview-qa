---
id: emb-cppoop-0001
title: "What does \"zero-overhead abstraction\" mean for a C++ class?"
description: "A non-virtual class compiles to the same code as a C struct with free functions when the optimizer sees the method bodies."
track: embedded
section: cpp-classes-and-oop
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

**A non-virtual class can compile to the same machine code as a C struct with free functions, provided the optimizer sees the method bodies.**

A non-static member function effectively receives an implicit `this`; without `virtual` there is no vtable/vptr, and simple methods are usually inlined. At `-O0` or across separate translation units, the call may remain a regular call.

Rule: encapsulation via a class in embedded is usually free in a release build, as long as there are no virtual functions or extra state.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
