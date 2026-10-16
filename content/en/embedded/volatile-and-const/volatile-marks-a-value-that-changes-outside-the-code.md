---
id: emb-volconst-0001
title: "What does the `volatile` qualifier mean in C?"
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

**`volatile`** qualifies an object whose accesses must be observable to the C implementation according to its rules for volatile accesses.

This usually prevents removal of needed accesses or reuse of a saved value. Exact access semantics depend on the compiler and platform. A memory-mapped register read can return peripheral state, and a write can trigger hardware.

Rule: use `volatile` for objects with externally observable accesses, not as a general synchronisation mechanism or an atomicity guarantee.[^iso-c-n1570]

## Detailed explanation

TODO
