---
id: emb-tmplcx-0034
title: "What should a candidate demonstrate on templates and constexpr questions?"
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

**Understanding of the compile-time vs runtime boundary, the ability to spot template bloat on a flash-constrained MCU, and when CRTP is better than virtual.**

Plus: `constexpr` for moving computations to build time, `if constexpr` as a type-safe `#ifdef`, strategies against bloat, and verification via the linker map.

Rule: always distinguish zero runtime cost from real Flash and compile cost.[^embeddedinterviewlab]

## Detailed explanation

TODO
