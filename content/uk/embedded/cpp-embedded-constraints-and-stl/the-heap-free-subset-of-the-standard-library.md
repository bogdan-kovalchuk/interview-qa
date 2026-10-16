---
id: emb-cppstl-0009
title: "Які STL-компоненти безпечні (heap-free) для embedded?"
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

**`std::array`, `std::optional`, `std::string_view`, `std::bitset`, `std::tuple`/`std::pair`, `std::variant`, ``, ``.**

Усі вони мають фіксований розмір або працюють на ітераторах без алокації. `std::sort`, `std::find`, `std::accumulate` – header-only, без heap.

Правило: STL (standard template library) не заборонена цілком – безпечна її heap-free підмножина.[^embeddedinterviewlab]

## Detailed explanation

TODO
