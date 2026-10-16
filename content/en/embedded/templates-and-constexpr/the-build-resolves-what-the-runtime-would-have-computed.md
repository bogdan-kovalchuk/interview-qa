---
id: emb-tmplcx-0026
title: "What does \"zero-cost abstraction\" mean for templates and constexpr?"
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

**The compiler resolves types and computes values at build time – after optimisation the code can be as tight as hand-written C, but with stronger type safety.**

Important: this applies to the runtime cost of a well-designed abstraction; flash footprint and compile time carry a real price.

Rule: zero-cost means no mandatory runtime price, but not free in Flash and build time.[^embeddedinterviewlab]

## Detailed explanation

TODO
