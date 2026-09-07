---
id: emb-cppoop-0003
title: "What is the implicit `this` pointer?"
description: "A hidden parameter of every non-static member function, holding the address of the object it was called on."
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

**A hidden parameter of every non-static member function – the address of the object it was called on.**

`obj.set()` compiles roughly as a function call that receives `&obj`. That is why a member function sees the object's fields without a prefix.

Rule: `this` makes a member function close to a C function with an explicit pointer to a struct; the optimizer can reduce the difference to zero.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
