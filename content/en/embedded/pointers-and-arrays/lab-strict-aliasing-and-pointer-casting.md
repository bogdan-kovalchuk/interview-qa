---
id: emb-cppfound-0077
title: "What is the strict aliasing rule, and how does it apply to pointer casts?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Strict aliasing rule** (C99/C11 §6.5): the compiler assumes that pointers of incompatible types do not address the same memory. This allows aggressive optimization: writing through `float*` does not force the compiler to reload the value through `int*`. Exception: character types (`char*`, `unsigned char*`, `uint8_t*`) may alias any object. Violation: `int x; float *fp = (float*)&x; *fp = 1.0f;` causes UB. Safe type punning: `memcpy` or `union` (in C).[^embeddedinterviewlab]

## Detailed explanation

TODO
