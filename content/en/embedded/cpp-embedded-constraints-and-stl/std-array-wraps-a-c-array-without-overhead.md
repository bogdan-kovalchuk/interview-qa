---
id: emb-cppstl-0011
title: "How is `std::array` better than a raw C array?"
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

**Zero-overhead wrapper over a C array with `.size()`, `.at()` (with bounds checking) and compatibility with ``.**

It does not decay to a pointer when passed, knows its size and works with `std::sort`/`std::find`. Size and layout are identical to a C array.

Rule: in C++ embedded `std::array` fully replaces `T[]` as the default container.[^embeddedinterviewlab]

## Detailed explanation

TODO
