---
id: emb-cppfound-0028
title: "What is `restrict` and why is it useful in embedded systems?"
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

`restrict` (C99) – a pointer qualifier that promises the compiler: through this pointer and through no other pointer in this function **does aliasing occur** (no overlapping memory regions).

Example: `void add(int * restrict dst, const int * restrict src, int n)`.

Gives the compiler freedom for aggressive optimization (vectorization, register promotion). Important for DSP, crypto, memcpy-like functions. If aliasing does occur – undefined behavior.[^embeddedinterviewlab]

## Detailed explanation

TODO
