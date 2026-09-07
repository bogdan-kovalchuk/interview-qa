---
id: emb-cppoop-0027
title: "Does a class without any virtual function still pay virtual overhead?"
description: "Without any virtual function a class has neither a vtable nor a vptr and pays no overhead"
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

**No – without any virtual function the class has neither a vtable nor a vptr.**

`sizeof` such an object equals the sum of its fields (+ padding), just like a C struct. The overhead appears only with the first virtual function.

Rule: encapsulate freely; you pay for polymorphism only when you actually declare `virtual`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
