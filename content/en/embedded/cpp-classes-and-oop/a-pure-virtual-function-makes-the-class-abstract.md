---
id: emb-cppoop-0016
title: "What is a pure virtual function and an abstract class?"
description: "A pure virtual function declared with = 0 makes its class abstract and uninstantiable"
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

## Question code

```cpp
class Sensor {
public:
  virtual int16_t read() = 0;
  virtual ~Sensor() = default;
};
```

## Short answer

**`= 0` makes a function pure virtual; a class containing one becomes abstract and cannot be instantiated.**

An abstract class defines an interface (contract) that derived classes must implement. Polymorphic derived objects will have vptr/vtable; the abstract base object itself cannot be created.

Rule: an abstract base is the C++ way to describe a driver/HAL (hardware abstraction layer) interface.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
