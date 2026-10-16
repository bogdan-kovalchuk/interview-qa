---
id: emb-cppstl-0025
title: "Which C++ standard is the embedded sweet spot today and why?"
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

**C++17.**

It provides `if constexpr` (zero-cost compile-time branches), `std::optional`/`std::variant` (safe value types) and `std::string_view` (zero-copy strings) – all without the heap.

Rule: C++17 is the practical balance of modern features and toolchain support for MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO
