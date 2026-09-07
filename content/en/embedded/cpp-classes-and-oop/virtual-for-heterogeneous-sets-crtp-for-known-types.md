---
id: emb-cppoop-0021
title: "CRTP versus virtual: when do you choose which?"
description: "Virtual suits heterogeneous collections with runtime dispatch; CRTP suits fixed types at maximum speed"
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

**Virtual** – heterogeneous collections (an array of `Base*` with different types), dispatch at runtime, one copy of the base code.

CRTP (Curiously Recurring Template Pattern) – fixed types, performance-critical: compile-time dispatch, no vtable/vptr, predictable direct calls. The price is duplication of the base code for every derived type.

Rule: different types in one container -> virtual; maximum speed with known types -> CRTP.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
