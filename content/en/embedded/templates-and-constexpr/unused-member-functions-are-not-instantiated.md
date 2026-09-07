---
id: emb-tmplcx-0032
title: "Does the compiler generate code for unused member functions of a template?"
description: "Usually no, only member functions that are actually needed are generated during implicit instantiation of a class template."
track: embedded
section: templates-and-constexpr
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

**Usually no – during implicit instantiation of a class template, only the member functions that are actually needed are generated.**

This limits bloat: if `pop()` is never called on `CircularBuffer<T,N>`, its code typically does not end up in Flash for that instantiation. Exceptions: explicit instantiation, virtual functions, and other ODR-use scenarios can force more code to be generated.

Rule: unused template methods are often free, but check the linker map for template-heavy code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
