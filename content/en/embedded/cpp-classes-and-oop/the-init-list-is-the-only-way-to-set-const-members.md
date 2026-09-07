---
id: emb-cppoop-0006
title: "What is a member initialisation list in a constructor for?"
description: "It initializes members before the constructor body, and is the only way to initialize const and reference members."
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
Gpio(uint32_t base, uint8_t pin)
  : odr_{(volatile uint32_t*)(base + 0x14)}, pin_{pin} {}
```

## Short answer

**It initializes members before entering the constructor body – the only way for `const` and reference members.**

`const uint8_t pin_` cannot be assigned in the body; it must be initialized in the list. This is also more efficient: direct initialization instead of "default + assignment".

Rule: initialize all members in the list, in the order they are declared in the class.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
