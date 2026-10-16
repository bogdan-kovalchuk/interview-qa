---
id: emb-cppstl-0022
title: "Trap: what happens on an out-of-bounds `vector::at()` under `-fno-exceptions`?"
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

<span class="warn">In many embedded toolchains, instead of throwing `std::out_of_range`, the library path ends in `abort()` or another fatal handler.</span>

`-fno-exceptions` does not remove the bounds check; it changes the reaction to failure. On an MCU this often looks like an emergency stop or a HardFault with no proper diagnostics.

Protection: use `std::array` or a custom bounds-checking wrapper that logs data before stopping.[^embeddedinterviewlab]

## Detailed explanation

TODO
