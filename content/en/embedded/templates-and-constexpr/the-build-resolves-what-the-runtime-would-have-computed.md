---
id: emb-tmplcx-0026
title: "What does \"zero-cost abstraction\" mean for templates and constexpr?"
description: "The compiler resolves types and computes values at build time, so after optimisation the code can be as tight as hand-written C with stronger type safety."
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

**The compiler resolves types and computes values at build time – after optimisation the code can be as tight as hand-written C, but with stronger type safety.**

Important: this applies to the runtime cost of a well-designed abstraction; flash footprint and compile time carry a real price.

Rule: zero-cost means no mandatory runtime price, but not free in Flash and build time.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
