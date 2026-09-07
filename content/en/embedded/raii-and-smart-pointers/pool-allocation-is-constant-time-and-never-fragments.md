---
id: emb-raii-0017
title: "What is arena or pool allocation in the context of RAII?"
description: "Allocation from a fixed-size array: O(1) cost, zero fragmentation, controlled lifetime."
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

**Allocation from a fixed-size array: O(1) cost, zero fragmentation, controlled lifetime.**

Instead of many `malloc`/`free` calls, blocks are taken from a pool. If the objects are trivial, the phase can end with an arena reset; if the objects have non-trivial destructors, they must be called before the reset.

Rule: pool allocation gives determinism and zero fragmentation, which is what the heap lacks in embedded.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
