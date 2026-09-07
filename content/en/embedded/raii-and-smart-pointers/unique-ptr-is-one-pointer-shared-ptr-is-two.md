---
id: emb-raii-0022
title: "How do `unique_ptr` and `shared_ptr` differ in size?"
description: "uniqueptr with stateless deleter is usually the size of a raw pointer; sharedptr is usually two pointers plus a separate control block."
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

**`unique_ptr` (with a stateless deleter) is usually the size of a raw pointer; `shared_ptr` is usually two pointers plus a separate control block.**

`shared_ptr` stores a pointer to the object and a pointer to the control block (where the counters are), plus the control block itself is on the heap or in an allocation created by `make_shared`. The exact size depends on the STL implementation and ABI.

Rule: one owner -> `unique_ptr`; shared -> `shared_ptr` (you pay with memory, counters and often atomics).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
