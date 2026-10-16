---
id: emb-align-0025
title: "What does `_Alignof(T)` (C11) / `alignof(T)` return?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**The alignment requirement of the type, in bytes.**

Values for `uint32_t` and `double` depend on the implementation; the often quoted 4 and 8 are not standard guarantees. This compile-time property is useful for layout checks and custom allocators.

Rule: in C11 use `_Alignof` (the `alignof` macro in `<stdalign.h>`); in C++ `alignof` is built-in.[^iso-c-n1570]

## Detailed explanation

TODO
