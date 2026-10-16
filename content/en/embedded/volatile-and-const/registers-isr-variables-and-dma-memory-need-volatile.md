---
id: emb-volconst-0003
title: "Name three typical use cases for `volatile` in embedded C."
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
---

## Short answer

Three typical use cases: memory-mapped hardware registers, variables shared with an ISR, and memory modified by DMA.

In all three cases the compiler does not see an ordinary C write that changes the value. Without `volatile` it may cache the old value or remove the access as redundant.

These are not universally mandatory cases: ISR and DMA rules depend on the compiler and platform, and `volatile` alone does not provide synchronisation.[^iso-c-n1570] [^gcc-volatile]

## Detailed explanation

TODO
