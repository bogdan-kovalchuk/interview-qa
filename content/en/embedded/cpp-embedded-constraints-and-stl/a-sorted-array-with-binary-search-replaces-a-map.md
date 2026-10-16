---
id: emb-cppstl-0028
title: "How do you replace `std::map` without a heap?"
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

**A sorted `std::array` of pairs + binary search (`std::lower_bound`).**

`std::map` allocates nodes on the heap for every insertion. If the key set is known at compile time, a `constexpr` sorted array gives O(log n) lookup without any allocation.

Rule: static lookup tables – sorted `array` + binary search instead of `map`.[^embeddedinterviewlab]

## Detailed explanation

TODO
