---
id: emb-raii-0026
title: "Trap: why is forgetting `= delete` on the copy constructor of a resource wrapper critical?"
description: "The default copy constructor makes a shallow handle copy so two objects own one resource, causing double free."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
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

<span class="warn">The default copy ctor makes a shallow copy of the handle -> two objects own one resource -> double free.</span>

On destruction of both, the dtor frees the mutex/DMA/handle twice – UB (undefined behavior), corruption, or closing an already closed resource.

Defense: for resource wrappers, always either `= delete` copy or implement move semantics with zeroing the source.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
