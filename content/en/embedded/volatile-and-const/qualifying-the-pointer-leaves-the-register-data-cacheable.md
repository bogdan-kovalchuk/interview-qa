---
id: emb-volconst-0011
title: "Trap: why is `uint32_t * volatile reg` the wrong type for hardware register data?"
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

<span class="warn">`volatile` applies to the pointer variable, not to the data at the address.</span>

`volatile` qualifies accesses to the pointer variable itself, while `*reg` still has the plain type `uint32_t`. Therefore access to the register data is not volatile-qualified and does not get volatile access semantics.[^iso-c-n1570]

Fix: use `volatile uint32_t *reg` for a pointer to volatile data, or `volatile uint32_t * const reg` if the address is fixed.[^iso-c-n1570]

## Detailed explanation

TODO
