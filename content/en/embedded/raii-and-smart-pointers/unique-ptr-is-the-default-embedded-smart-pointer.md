---
id: emb-raii-0032
title: "Why is `unique_ptr` considered the default smart pointer for embedded?"
description: "Zero overhead like a raw pointer, exclusive ownership, explicit transfer via move, and custom deleter support for HAL."
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

**Zero overhead (like a raw pointer), exclusive ownership, explicit transfer via move, custom deleter support for HAL.**

It covers the vast majority of ownership scenarios without the cost of `shared_ptr` (control block, atomics, heap).

Rule: start with `unique_ptr`; move to `shared_ptr` only when shared ownership is genuinely needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
