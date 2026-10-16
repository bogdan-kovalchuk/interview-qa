---
id: emb-tmplcx-0029
title: "Як constexpr дає compile-time bounds checking?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Коли розмір – NTTP, індекси/межі можна перевірити `static_assert`-ом на етапі компіляції.**

Напр. `get<I>()` з `static_assert(I < N, "out of range")` зробить вихід за межі compile error, а не runtime-багом.

Правило: переноси перевірку меж у compile time скрізь, де індекс/розмір відомі статично.[^embeddedinterviewlab]

## Detailed explanation

TODO
