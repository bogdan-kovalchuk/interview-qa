---
id: emb-raii-0031
title: "How does move semantics let an RAII object be returned from a function?"
description: "The move constructor transfers resource ownership without copying and without double release."
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

**The move ctor transfers resource ownership without copying and without double release.**

`return guard;` for a move-only type moves the handle to the caller, zeroing the source, so the source dtor frees nothing. This lets factory functions hand out ready-made RAII resources.

Rule: move-only RAII can be returned from functions; copy is forbidden to avoid double release.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
