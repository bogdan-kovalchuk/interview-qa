---
id: emb-volconst-0004
title: "Trap: does `volatile` make an operation atomic?"
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

<span class="warn">No. `volatile` does not guarantee atomicity.</span> For example, a `volatile uint32_t` on an 8-bit MCU may be read in several instructions, and an ISR can fire between them; even if a single `counter` read is atomic on a particular Cortex-M, `counter++` consists of a read, computation, and write.

Mitigation: for shared state use atomic operations, a critical section, or platform primitives chosen for the required guarantee.[^iso-c-n1570]

## Detailed explanation

TODO
