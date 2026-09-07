---
id: emb-cppstl-0006
title: "Which allocation strategies are used instead of the heap?"
description: "Static allocation, placement new, fixed-size memory pools and stack allocation"
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Static allocation, placement new, fixed-size memory pools, stack allocation.**

All objects have static/automatic storage; there is no `new`/`delete`. A pool gives O(1) with no fragmentation; the stack is for locals, but small (stacks 1–4 KB).

Rule: in safety-critical embedded the heap is either forbidden or used only during initialisation.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
