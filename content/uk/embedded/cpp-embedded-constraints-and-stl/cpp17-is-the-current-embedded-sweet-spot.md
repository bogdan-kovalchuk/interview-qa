---
id: emb-cppstl-0025
title: "Який стандарт C++ – «sweet spot» для embedded сьогодні і чому?"
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

Дає `if constexpr` (zero-cost compile-time гілки), `std::optional`/`std::variant` (безпечні value-типи) і `std::string_view` (zero-copy рядки) – усе без heap.

Правило: C++17 – практичний баланс сучасних фіч і toolchain-підтримки для MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO
