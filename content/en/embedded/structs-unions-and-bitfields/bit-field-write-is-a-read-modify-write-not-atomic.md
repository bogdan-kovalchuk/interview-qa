---
id: emb-structs-0049
title: "Trap: can a bit-field be used as an atomic flag between an ISR and main?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Writing a bit-field is typically a read-modify-write of the storage unit, so it should not be used as an atomic flag between an ISR and main. If both contexts modify different bit-fields in the same storage unit, one write can clobber the other. `volatile` does not make this operation atomic.

Mitigation: use separate flags only when accesses are atomic on the target; otherwise use a critical section or RTOS event flags. `volatile` alone guarantees neither atomicity nor synchronization.[^iso-c-n1570]

## Detailed explanation

TODO
