---
id: emb-raii-0010
title: "Why is `shared_ptr` rarely used in embedded?"
description: "sharedptr adds a control block per object, atomic reference counting on every copy and destroy, and usually a heap allocation, with non-deterministic cleanup timing."
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

<span class="warn">Expensive: a control block per object, reference counting on copy/assign/destroy, and usually heap allocation.</span>

The control block size is implementation-defined, but it is certainly not just one pointer. Plus non-determinism: cleanup happens only when the last owner is destroyed, and it is not always obvious where that will be.

Rule: on bare metal without a heap, avoid `shared_ptr`; for a single owner, use `unique_ptr`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
