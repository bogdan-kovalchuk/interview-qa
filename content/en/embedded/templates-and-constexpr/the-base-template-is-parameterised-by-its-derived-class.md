---
id: emb-tmplcx-0011
title: "What is CRTP and what is it for in templates?"
description: "CRTP is a pattern where a base class template is parameterized by the derived class."
track: embedded
section: templates-and-constexpr
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
template<typename D>
class SensorBase {
public:
  int read_filtered() {
    int raw = static_cast<D*>(this)->read_raw();
    return (raw + last_) / 2;
  }
};
```

## Short answer

**CRTP (curiously recurring template pattern): the base is a template parameterized by the derived class: `class Derived : public Base`.**

The base calls derived methods through `static_cast<D*>(this)`, which resolves at compile time – polymorphism without a vtable.

Rule: CRTP gives a "virtual" structure without virtual dispatch; after optimization it often has no additional runtime overhead.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
