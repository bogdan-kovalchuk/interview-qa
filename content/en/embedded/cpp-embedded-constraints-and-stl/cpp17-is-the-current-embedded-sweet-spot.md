---
id: emb-cppstl-0025
title: "Which C++ standard is the current embedded sweet spot and why?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: misra-cpp-2023
    title: "MISRA C++:2023 Guidelines for the use of the C++17 language in critical systems"
    url: https://www.misra.org.uk/
---

## Short answer

**C++17.**

Provides `if constexpr` (zero-cost compile-time branching), `std::optional`/`std::variant` (safe value types), and `std::string_view` (zero-copy strings) – all without a heap.

Rule: C++17 is the practical balance of modern features and toolchain support for MCUs.[^embeddedinterviewlab]

## Detailed explanation

TODO
