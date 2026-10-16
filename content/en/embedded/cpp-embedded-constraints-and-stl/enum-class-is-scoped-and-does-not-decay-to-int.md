---
id: emb-cppstl-0029
title: "Why is `enum class` better than a plain `enum` for statuses?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Scoped and strongly typed: it does not implicitly convert to `int` and does not pollute the namespace.**

`Status::Ok` cannot be confused with another enum, and `if (status)` does not accidentally compile. This catches an entire class of comparison/conversion bugs.

Rule: for error codes and statuses use `enum class`, not a bare `enum`.[^embeddedinterviewlab]

## Detailed explanation

TODO
