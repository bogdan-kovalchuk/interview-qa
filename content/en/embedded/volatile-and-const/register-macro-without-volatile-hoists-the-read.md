---
id: emb-volconst-0007
title: "Trap: what is wrong with this polling code?"
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

## Question code

```c
#define UART_SR (*( uint32_t *)0x40011000)

while ((UART_SR & 0x20) == 0) { }
```

## Short answer

<span class="warn">The memory-mapped register access is not `volatile`.</span>

`UART_SR` dereferences a plain `uint32_t *`, so the C compiler is not required to treat each access as volatile; an optimisation may remove repeated reads. In a release build, polling may then miss a change to the status register.[^iso-c-n1570]

Use `#define UART_SR (*(volatile uint32_t *)0x40011000u)` and check that the address and access width match the MCU documentation. `volatile` does not prove that the address is correct or that the peripheral supports that access.[^iso-c-n1570]

## Detailed explanation

TODO
