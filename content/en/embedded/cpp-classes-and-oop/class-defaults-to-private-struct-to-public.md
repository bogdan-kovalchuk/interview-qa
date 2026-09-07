---
id: emb-cppoop-0002
title: "How does `class` differ from `struct` in C++?"
description: "The main difference is default access: class is private, struct is public; default inheritance differs the same way."
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

**The main difference is default access: `class` is private, `struct` is public.**

Default inheritance also differs: `class Derived : Base` inherits private, while `struct Derived : Base` inherits public. Otherwise, both can equally have methods, constructors, and inheritance.

Convention: `struct` is for simple POD-like (plain old data) aggregates, `class` is used when there are invariants and encapsulation.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
