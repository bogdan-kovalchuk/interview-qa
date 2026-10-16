---
id: emb-cppstl-0031
title: "Trap: why is a raw C array in a C++ signature a bad signal in an interview?"
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

<span class="warn">It decays to a pointer (losing the size) and shows ignorance of modern practices.</span>

`void f(int arr[])` actually takes `int*`; `sizeof` inside gives the pointer size. `std::array`/`std::span` preserve the size and are safer.

Protection: in C++ pass `std::array&`, `std::span` or (container + size), not a bare `T[]`.[^embeddedinterviewlab]

## Detailed explanation

TODO
