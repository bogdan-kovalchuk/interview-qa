---
id: emb-tmplcx-0005
title: "What is a constexpr function?"
description: "A function evaluable at compile time when inputs are constant, and at runtime otherwise."
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

**A function that can be evaluated at compile time when its inputs are constant, and at runtime otherwise.**

This enables zero-runtime-cost lookup tables, configuration values and computations: the result can land in Flash/`.rodata` as a ready constant if the object has appropriate static storage.

Rule: `constexpr` moves computation from runtime to build time where the result is genuinely needed as a constant expression.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
