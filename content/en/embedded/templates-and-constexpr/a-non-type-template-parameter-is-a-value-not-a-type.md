---
id: emb-tmplcx-0004
title: "What is a non-type template parameter (NTTP)?"
description: "A template parameter that is a value (not a type), e.g. sizet N."
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

**A template parameter that is a value (not a type) – e.g. `size_t N`.**

In `CircularBuffer<T, N>` the size `N` is an NTTP: the compiler knows it at build time, so it can allocate a fixed-size array and fold computations into constants.

Rule: NTTP lets you bake sizes/configuration into the type and get compile-time bounds checking.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
