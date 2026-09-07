---
id: emb-raii-0012
title: "When is `shared_ptr` nevertheless justified in embedded?"
description: "When there is genuine shared ownership and heap plus atomics are available."
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

**When there is genuine shared ownership and heap plus atomics are available.**

Examples: reference-counted buffers in embedded Linux userspace, plugin and modular systems with shared config blocks, objects whose lifetime truly has no single owner. For DMA (direct memory access) buffers in bare-metal, an explicit owner plus borrowed views is usually better.

Rule: `shared_ptr` is only for real shared ownership, not just in case.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
