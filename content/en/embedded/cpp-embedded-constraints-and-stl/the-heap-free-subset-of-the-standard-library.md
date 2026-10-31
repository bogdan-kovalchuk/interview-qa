---
id: emb-cppstl-0009
title: "Which STL components are safe (heap-free) for embedded?"
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

**`std::array`, `std::optional`, `std::string_view`, `std::bitset`, `std::tuple`/`std::pair`, `std::variant`, `<algorithm>`, `<numeric>`.**

All of them have fixed size or work on iterators without allocation. `std::sort`, `std::find`, `std::accumulate` are header-only, no heap.

Rule: STL (standard template library) is not forbidden entirely – its heap-free subset is safe.[^embeddedinterviewlab]

## Detailed explanation

TODO
