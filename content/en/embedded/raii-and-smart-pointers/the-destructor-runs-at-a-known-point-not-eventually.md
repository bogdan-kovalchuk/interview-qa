---
id: emb-raii-0028
title: "Why does RAII give deterministic destruction while garbage collection does not?"
description: "The destructor runs at a precisely known moment, at scope exit."
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

**The destructor runs at a precisely known moment, at scope exit.**

Unlike GC (garbage collection), where the moment of release is indeterminate, RAII releases the resource immediately and predictably, which is critical for real-time and hardware resources (a port is occupied exactly until the end of the scope).

Rule: deterministic teardown is the main reason embedded relies on RAII rather than GC-like approaches.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
