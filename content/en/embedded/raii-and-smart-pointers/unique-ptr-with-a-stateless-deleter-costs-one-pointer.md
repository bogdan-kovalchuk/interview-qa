---
id: emb-raii-0008
title: "What overhead does `unique_ptr` have compared with a raw pointer?"
description: "With a stateless deleter, uniqueptr has the size of one raw pointer, no control block, and no reference counting; the compiler usually inlines the teardown call."
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

**With a stateless deleter, `unique_ptr` usually has the size of one raw pointer.**

There is no control block and no reference counting. The deleter type is known at compile time, so the compiler often inlines the teardown call. If the deleter has state or is a function pointer, `sizeof(unique_ptr)` can grow.

Rule: `unique_ptr` is the default smart pointer in embedded; to keep zero size overhead, keep the deleter stateless.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
