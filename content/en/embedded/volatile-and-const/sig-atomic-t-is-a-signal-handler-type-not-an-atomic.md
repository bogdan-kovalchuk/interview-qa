---
id: emb-volconst-0044
title: "Trap: does `volatile sig_atomic_t` give the same guarantees as a hardware atomic?"
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

<span class="warn">No. `volatile sig_atomic_t` has a narrow C guarantee for signal handling; it is not a universal atomic primitive for MCU ISRs.</span>[^iso-c-n1570]

In C, `sig_atomic_t` is intended for atomic access in the signal-handling context. This does not make an arbitrary `volatile` type on an MCU atomic, or establish memory ordering between an ISR and main code.

On an MCU, check atomic access width in the CPU and ABI documentation; protect more complex communication with supported atomic operations or critical sections.[^iso-c-n1570]

## Detailed explanation

TODO
