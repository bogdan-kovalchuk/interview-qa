---
id: emb-cppstl-0022
title: "Trap: `vector::at()` out of bounds with `-fno-exceptions` – what happens?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-cxx-dialect
    title: "GCC: C++ Dialect Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html
---

## Short answer

<span class="warn">In many embedded toolchains, instead of throwing `std::out_of_range` the library path ends in `abort()` or another fatal handler.</span>

`-fno-exceptions` does not remove the bounds check; only the failure response changes. On an MCU this often looks like an abnormal halt or HardFault without proper diagnostics.

Protection: use `std::array` or a custom bounds-checking wrapper that logs state before halting.[^embeddedinterviewlab]

## Detailed explanation

TODO
