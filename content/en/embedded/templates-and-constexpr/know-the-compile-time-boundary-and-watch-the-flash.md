---
id: emb-tmplcx-0034
title: "What should a candidate demonstrate on templates and constexpr questions?"
description: "Understanding of the compile-time vs runtime boundary, ability to spot template bloat on a flash-constrained MCU, and when CRTP beats virtual."
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

**Understanding of the compile-time vs runtime boundary, the ability to spot template bloat on a flash-constrained MCU, and when CRTP is better than virtual.**

Plus: `constexpr` for moving computations to build time, `if constexpr` as a type-safe `#ifdef`, strategies against bloat, and verification via the linker map.

Rule: always distinguish zero runtime cost from real Flash and compile cost.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
