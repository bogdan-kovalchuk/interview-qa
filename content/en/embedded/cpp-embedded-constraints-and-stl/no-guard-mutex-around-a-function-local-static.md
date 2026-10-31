---
id: emb-cppstl-0020
title: "What does `-fno-threadsafe-statics` do?"
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
    title: "Itanium C++ ABI: Once-only Construction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#once-ctor
---

## Short answer

**Removes mutex protection around function-local static initialization.**

By default the compiler adds a guard (possibly with pthread) so two threads do not initialise the static at once. On bare-metal without threads this is dead code and a dependency.

Rule: `-fno-threadsafe-statics` is appropriate when there is no concurrent access to the lazy-init static (single-threaded bare-metal).[^embeddedinterviewlab]

## Detailed explanation

TODO
