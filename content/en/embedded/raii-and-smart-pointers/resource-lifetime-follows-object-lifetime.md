---
id: emb-raii-0001
title: "What is RAII and what does the acronym stand for?"
description: "RAII ties a resource lifetime to a C++ object lifetime so the constructor acquires and the destructor releases, with cleanup guaranteed on scope exit."
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

**RAII (Resource Acquisition Is Initialization)** – the resource lifetime is tied to the C++ object lifetime.

The constructor acquires the resource, the destructor releases it. The compiler guarantees cleanup on scope exit: normal path, early `return`, and – if exceptions are enabled – stack unwinding.

Rule: anything that must be taken and given back, wrap in an object with a ctor/dtor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
