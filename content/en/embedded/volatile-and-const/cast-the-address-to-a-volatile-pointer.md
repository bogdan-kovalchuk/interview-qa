---
id: emb-volconst-0008
title: "How do you correctly declare a memory-mapped 32-bit register at `0x40020014`?"
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

Typical form: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`.[^iso-c-n1570]

Here `volatile uint32_t *` means pointer to volatile 32-bit data. Dereferencing it produces a volatile lvalue whose access preserves implementation-defined volatile semantics; mapping that to a physical bus access depends on the MCU and compiler.[^iso-c-n1570]

This is a common form for a memory-mapped register, but check the address and permitted access width against the MCU documentation.[^iso-c-n1570]

## Detailed explanation

TODO
