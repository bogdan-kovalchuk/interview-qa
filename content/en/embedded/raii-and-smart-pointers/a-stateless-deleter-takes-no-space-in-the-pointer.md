---
id: emb-raii-0023
title: "Why should a custom deleter be stateless?"
description: "A stateless deleter type may occupy no space in uniqueptr thanks to empty base optimization."
track: embedded
section: raii-and-smart-pointers
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

**A stateless deleter type (a lambda without capture or an empty functor) may occupy no space in `unique_ptr` thanks to empty base optimization.**

A capturing lambda carries state, so it increases `sizeof(unique_ptr)` and may defeat the optimization. A function pointer deleter also has no object state, but the pointer itself must be stored in `unique_ptr`, so the size usually becomes two pointers.

Rule: a deleter without runtime state -> `unique_ptr` can stay the size of a raw pointer; a function pointer deleter is simple but not size-free.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
