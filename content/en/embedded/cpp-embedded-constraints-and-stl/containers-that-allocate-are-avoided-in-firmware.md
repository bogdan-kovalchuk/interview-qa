---
id: emb-cppstl-0010
title: "Which STL components are avoided in embedded and why?"
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

<span class="warn">`std::vector`, `std::string`, `std::map`/`unordered_map`, `std::shared_ptr`, `<iostream>` – they often pull in the heap or heavy runtime infrastructure.</span>

`vector`/`string` typically allocate a dynamic array; `map` uses nodes on the heap; `shared_ptr` has a control block; `<iostream>` can pull in locales, buffers and tens of KB of Flash depending on the library.

Rule: replace with `std::array`, `std::string_view`/`char[]`, a sorted `array` + binary search.[^embeddedinterviewlab]

## Detailed explanation

TODO
