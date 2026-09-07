---
id: emb-cppoop-0034
title: "Why should an abstract base declare its virtual destructor `= default`?"
description: "It ensures correct polymorphic destruction without a hand-written empty body"
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
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

## Question code

```c
virtual ~Sensor() = default;
```

## Short answer

**It ensures correct polymorphic destruction without a hand-written empty body.**

`= default` asks the compiler to generate the destructor; with `virtual` it is not trivial in the strict sense, but the code can still be empty and optimised. `virtual` guarantees that `delete base_ptr` calls the derived dtor.

Rule: for an interface base use `virtual ~T() = default;` when polymorphic delete is possible; for global objects remember that a non-trivial dtor may trigger `atexit` registration.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
