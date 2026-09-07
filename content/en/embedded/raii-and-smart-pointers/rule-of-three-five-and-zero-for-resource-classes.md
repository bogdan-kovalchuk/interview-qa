---
id: emb-raii-0025
title: "What are the rule of three, five and zero?"
description: "If a class manages a resource, define or delete all special functions together."
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

**If a class manages a resource, define or delete all special functions together.**

Rule of three: dtor, copy ctor, copy assign. Rule of five (C++11): plus move ctor, move assign. Rule of zero: do not manage resources manually, let RAII members (smart pointers, guards) do it, and write no special function at all.

Rule: aim for the rule of zero; if you manage a resource yourself, do not leave the default copy operations that would cause double-free.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
