---
id: emb-volconst-0002
title: "How does `volatile` affect accesses optimised by the compiler?"
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

**`volatile` requires volatile accesses to be handled according to the C implementation's rules, so a compiler usually cannot cache them as ordinary values or remove them.**

Without it, a compiler may reuse an ordinary object's previous value or remove an unobservable store. `volatile` does not order ordinary accesses relative to volatile ones, nor does it prohibit every reordering.[^iso-c-n1570] [^gcc-volatile]

Rule: for precise ordering of peripheral operations, consult the compiler documentation and use the required compiler or hardware barrier.[^gcc-volatile]

## Detailed explanation

TODO
