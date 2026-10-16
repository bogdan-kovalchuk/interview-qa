---
id: emb-cppstl-0014
title: "Чому `<algorithm>` і `<numeric>` безпечні навіть без heap?"
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

**Вони працюють на ітераторах, а не на контейнерах – не алокують пам'ять самі.**

`std::sort`, `std::find`, `std::copy`, `std::accumulate` оперують діапазоном `[begin, end)`, тож їх можна застосовувати до `std::array` чи навіть C-масиву.

Правило: алгоритми STL – header-only й heap-free; небезпечні саме heap-контейнери, а не алгоритми.[^embeddedinterviewlab]

## Detailed explanation

TODO
