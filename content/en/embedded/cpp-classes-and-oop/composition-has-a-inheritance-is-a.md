---
id: emb-cppoop-0023
title: "Composition versus inheritance: what is the difference?"
description: "Composition is has-a with loose coupling; inheritance is is-a with tight coupling"
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

**Composition ("has-a")**: components are member objects, the parent delegates to them. Loose coupling, independent testing, easy mock substitution.

Inheritance ("is-a"): the derived implements the base interface. Tight coupling; testing requires mocking the entire base.

Rule: inheritance – for one-level interface abstraction; composition – for everything else.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
