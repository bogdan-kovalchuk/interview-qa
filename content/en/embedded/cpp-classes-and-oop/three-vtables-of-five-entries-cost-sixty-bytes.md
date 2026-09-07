---
id: emb-cppoop-0014
title: "Estimate the simplified cost: 3 classes with 5 virtual methods each. How much ROM for the vtables?"
description: "Three vtables times five entries times four bytes gives 60 bytes of ROM; vptrs add RAM per object"
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
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

**Rough estimate: 60 bytes of ROM (read-only memory)**: 3 vtables × 5 entries × 4 bytes on a 32-bit target.

In RAM (random-access memory), add a vptr per object: 100 objects × 4 bytes = 400 bytes of RAM just for vptrs. Actual ROM can be larger due to the ABI (application binary interface), RTTI or virtual destructors.

Rule: count the vtable per class, the vptr per instance; on a small MCU (microcontroller unit) it is vptr × number of objects that usually hurts most.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
