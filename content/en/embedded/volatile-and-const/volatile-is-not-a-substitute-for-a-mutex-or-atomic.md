---
id: emb-volconst-0052
title: "What does `volatile` mean for shared data in C: is it a replacement for a mutex or an atomic?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">No. `volatile` does not replace a mutex, an atomic, or RTOS synchronization.</span>

In C, `volatile` applies to accesses to volatile-qualified objects, but does not itself create a synchronizes-with relation between threads. C11 provides atomic operations for shared data between threads; an RTOS may also define its own synchronization mechanisms.[^iso-c-n1570]

Rule: use `volatile` when required by implementation rules for externally changed objects, and synchronization primitives for thread synchronization.[^iso-c-n1570]

## Detailed explanation

TODO
