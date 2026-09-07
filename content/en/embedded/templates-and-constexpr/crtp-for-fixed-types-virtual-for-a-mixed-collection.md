---
id: emb-tmplcx-0031
title: "When do you choose CRTP and when virtual in a template design?"
description: "CRTP suits fixed types and performance-critical code; virtual suits runtime polymorphism with heterogeneous collections."
track: embedded
section: templates-and-constexpr
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

**CRTP – fixed types, performance-critical (ISR, tight loops), with no virtual dispatch and no vtable on the object.**

Virtual – needed for runtime polymorphism: heterogeneous collections, plugins, dynamic driver loading. CRTP cannot hold different types in a single array without an additional type-erasure wrapper.

Rule: known types plus speed -> CRTP; different types at runtime -> virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
