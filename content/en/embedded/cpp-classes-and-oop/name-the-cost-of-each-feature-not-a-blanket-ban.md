---
id: emb-cppoop-0037
title: "What should a candidate say about C++ OOP in embedded?"
description: "Non-virtual classes can be zero-overhead; vtable lives in ROM, vptr costs RAM per instance"
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

**OOP (object-oriented programming) in embedded: non-virtual classes can be zero-overhead in release; vtable lives in ROM, vptr costs RAM per instance; CRTP gives compile-time polymorphism; composition is the default.**

Plus startup requirements: bare-metal must iterate `.init_array`; global destructors may pull in `atexit`; `-fno-exceptions`/`-fno-rtti` to control runtime support.

Rule: show that you know the cost of every feature in bytes and cycles, not just the syntax.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
