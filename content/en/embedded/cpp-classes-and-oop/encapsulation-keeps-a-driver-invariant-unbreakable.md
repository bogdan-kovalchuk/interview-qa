---
id: emb-cppoop-0033
title: "What is encapsulation and which guarantee does it give in a driver?"
description: "Hiding internal state behind a public interface so invariants cannot be violated from outside"
track: embedded
section: cpp-classes-and-oop
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

**Hiding internal state behind a public interface** so that invariants cannot be violated from outside.

A driver keeps registers/buffers private and exposes only validated operations; this costs nothing at runtime (as long as there are no virtuals) and makes entire classes of bugs impossible (raw access past checks).

Rule: encapsulation in embedded C++ is free safety, not an "academic" luxury.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
