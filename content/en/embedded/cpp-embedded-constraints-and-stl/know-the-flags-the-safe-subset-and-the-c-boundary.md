---
id: emb-cppstl-0035
title: "What should a candidate demonstrate about C++ constraints and the STL in embedded?"
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

**Why exceptions/RTTI are disabled, which STL subset is safe, how `extern "C"` works, placement new, and what MISRA C++ typically restricts.**

Plus: `std::array` as the default container, `std::optional`/`std::string_view` instead of null/`std::string`, and the fact that C++ provides zero-cost abstractions (not "heavy for embedded").

Rule: show specific flags, specific container replacements, and specific standards.[^embeddedinterviewlab]

## Detailed explanation

TODO
