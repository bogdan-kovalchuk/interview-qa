---
id: emb-cppstl-0019
title: "Which key compiler flags are used for embedded C++?"
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
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

They remove: exceptions, RTTI, static initialisation mutex (pthread), dtor registration via `__cxa_atexit`, and `.eh_frame` tables. Often paired with `-Os` and `-std=c++17`.

Rule: these flags make C++ deterministic and lean on bare metal.[^embeddedinterviewlab]

## Detailed explanation

TODO
