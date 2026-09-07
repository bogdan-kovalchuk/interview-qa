---
id: emb-cppoop-0020
title: "What is CRTP and which problem does it solve?"
description: "Curiously Recurring Template Pattern provides compile-time polymorphism via a static cast to the derived type"
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

```cpp
template <typename D>
class SensorBase {
public:
  int16_t read() {
    return static_cast<D*>(this)->read_impl();
  }
};
```

## Short answer

**Curiously Recurring Template Pattern – compile-time polymorphism** via `static_cast` to the derived type.

The derived class inherits `SensorBase<Derived>`. The compiler inlines `read_impl()` through the cast -> the same code as a direct call: no vtable, no vptr, no indirect call.

Rule: CRTP gives a "virtual" code structure with zero runtime overhead.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
