---
id: emb-cppoop-0007
title: "What is RAII in terms of constructors and destructors?"
description: "RAII ties resource lifetime to object lifetime: the constructor acquires the resource, the destructor releases it on scope exit."
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

**RAII (Resource Acquisition Is Initialization): the constructor acquires/configures the resource, the destructor automatically releases it on scope exit.**

For example: the ctor enables a clock and configures the peripheral, the dtor disables the clock or frees a DMA (direct memory access) channel. No chance of forgetting deinitialization – the compiler inserts the dtor call.

Rule: tie the resource lifetime (clock, DMA, lock) to the object lifetime – that is RAII.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
