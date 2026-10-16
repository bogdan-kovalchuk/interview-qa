---
id: emb-cppstl-0010
title: "Яких STL-компонентів уникають у embedded і чому?"
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

<span class="warn">`std::vector`, `std::string`, `std::map`/`unordered_map`, `std::shared_ptr`, `<iostream>` – вони часто тягнуть heap або важку runtime-інфраструктуру.</span>

`vector`/`string` зазвичай алокують динамічний масив; `map` – вузли в купі; `shared_ptr` – control block; `<iostream>` може тягнути locale, буфери й десятки КБ Flash залежно від бібліотеки.

Правило: заміняй на `std::array`, `std::string_view`/`char[]`, відсортований `array` + binary search.[^embeddedinterviewlab]

## Detailed explanation

TODO
