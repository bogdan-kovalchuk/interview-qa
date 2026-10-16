---
id: emb-dtypes-0046
title: "What's the difference: `volatile int *reg` vs `int * volatile reg`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`volatile int *reg` points to a `volatile int`, while `int * volatile reg` makes the pointer itself volatile; registers usually need the pointed-to type qualified. `volatile` requires accesses to be handled according to the C abstract machine, but does not by itself guarantee a physical bus transaction for every expression, atomicity, or synchronization.[^iso-c-n1570]

For example, `volatile uint32_t * const GPIOA` is a fixed pointer to a volatile object; the correct type and access rules depend on the MCU's register map.[^iso-c-n1570]

## Detailed explanation

TODO
