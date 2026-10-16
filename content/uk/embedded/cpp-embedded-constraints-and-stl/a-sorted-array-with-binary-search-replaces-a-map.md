---
id: emb-cppstl-0028
title: "Як замінити `std::map` без heap?"
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

**Відсортований `std::array` пар + binary search (`std::lower_bound`).**

`std::map` алокує вузли в купі на кожну вставку. Якщо набір ключів відомий на етапі компіляції, `constexpr` відсортований масив дає O(log n) пошук без жодної алокації.

Правило: статичні lookup-таблиці – sorted `array` + binary search замість `map`.[^embeddedinterviewlab]

## Detailed explanation

TODO
