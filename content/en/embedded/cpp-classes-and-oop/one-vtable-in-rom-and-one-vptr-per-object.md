---
id: emb-cppoop-0013
title: "What does a virtual function cost in memory?"
description: "One vtable per polymorphic class in ROM and one hidden vptr per polymorphic object in RAM"
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

**Typically a vtable – one per polymorphic class in ROM (read-only memory, `.rodata`), a vptr – one hidden pointer per polymorphic object in RAM (random-access memory).**

Rough estimate: vtable entries ≈ number of virtual functions × pointer size; vptr ≈ one pointer per instance. The exact layout depends on the ABI (application binary interface): destructors, RTTI or multiple inheritance can add entries.

Rule: count the vtable per class (ROM), the vptr per instance (RAM); with hundreds of objects the RAM cost becomes significant.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
