---
id: emb-cppstl-0021
title: "What does `-fno-use-cxa-atexit` do and why is it fine for MCUs?"
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
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor
---

## Short answer

**Does not register destructors of global objects via `__cxa_atexit`.**

On an MCU the program typically never exits, so dtors of globals are moot – registration only pulls in runtime infrastructure and ROM.

Rule: static objects on an MCU are "eternal"; `-fno-use-cxa-atexit` strips unneeded cleanup.[^embeddedinterviewlab]

## Detailed explanation

TODO
