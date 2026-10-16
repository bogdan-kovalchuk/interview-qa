---
id: emb-tmplcx-0027
title: "How is `static_assert` used with templates?"
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

**Compile-time checking of type and size invariants with a clear message.**

For example, in the default branch of `if constexpr`: `static_assert(always_false<P>, "Unsupported platform")` catches an unsupported type at compile time. Also `static_assert(N > 0, "...")` validates an NTTP.

Rule: `static_assert` is the primary tool for turning incorrect template usage into a clear error.[^embeddedinterviewlab]

## Detailed explanation

TODO
