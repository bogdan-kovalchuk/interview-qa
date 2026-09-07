---
id: emb-raii-0011
title: "What are the concrete costs of `shared_ptr`?"
description: "A sharedptr holds two pointers, one to the object and one to a control block with strong and weak counters plus deleter state; makeshared reduces allocations but does not remove the control block."
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

**Control block, reference counters, usually atomic increments/decrements, heap allocation, and a non-deterministic cleanup moment.**

A typical `shared_ptr` itself holds two pointers: a pointer to the object and a pointer to the control block. The control block stores strong/weak counters and deleter/allocator state. `make_shared` reduces the number of allocations but does not remove the control block.

Rule: in an interview, name the cost categories, not just "shared_ptr is slow."[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
