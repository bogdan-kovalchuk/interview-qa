---
id: emb-tmplcx-0031
title: "When do you choose CRTP and when virtual in a template design?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**CRTP – fixed types, performance-critical (ISR, tight loops), with no virtual dispatch and no vtable on the object.**

Virtual – needed for runtime polymorphism: heterogeneous collections, plugins, dynamic driver loading. CRTP cannot hold different types in a single array without an additional type-erasure wrapper.

Rule: known types plus speed -> CRTP; different types at runtime -> virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO
