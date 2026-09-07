---
id: emb-cppoop-0035
title: "Can you get polymorphism without the RAM overhead of a vptr?"
description: "CRTP resolves calls statically through staticcast, so the object contains no vptr"
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

**Yes – CRTP (Curiously Recurring Template Pattern, compile-time) or simply templates/composition.**

CRTP resolves calls statically through a `static_cast` to the derived type, so the object contains no vptr. This is ideal when the set of types is fixed at compile time.

Rule: you need polymorphism but vptr RAM (random-access memory) × many objects is too expensive -> use CRTP instead of virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
