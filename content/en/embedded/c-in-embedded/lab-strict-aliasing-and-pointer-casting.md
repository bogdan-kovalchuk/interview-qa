---
id: emb-cppfound-0077
title: "What is the strict aliasing rule, and how does it apply to pointer casts?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Strict aliasing rule** (C99 §6.5): the compiler may assume that pointers of different incompatible types do NOT alias (do not point to the same memory area). This allows aggressive optimization: if modified through `float*` – the compiler is not required to re-read through `int*`. Exception: `char*` and `unsigned char*` may alias anything. Violation: `int x; float *fp=(float*)&x; *fp=1.0f;` -> UB; protection: `memcpy` or `union` (in C).[^embeddedinterviewlab]

## Detailed explanation

TODO
