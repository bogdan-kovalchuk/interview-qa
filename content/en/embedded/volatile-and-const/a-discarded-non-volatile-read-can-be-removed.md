---
id: emb-volconst-0036
title: "Trap: what is wrong with reading a register and discarding the result?"
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
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
---

## Question code

```c
#define ADC_DR (*( uint32_t *)0x4001204C)

ADC_DR;
```

## Short answer

<span class="warn">If the register lvalue is not volatile-qualified, the compiler can remove the read.</span>

A data-register read may clear a flag or remove a FIFO sample; a plain `uint32_t` expression statement has no observable effect, so the compiler can remove it. GCC treats a discarded scalar volatile expression as a read, although the definition of a volatile access is implementation-defined.

Protection: declare an MMIO register through a volatile-qualified type, such as `(*(volatile uint32_t *)address)`. A `(void)` cast documents intent but does not make an ordinary object volatile.[^gcc-volatile]

## Detailed explanation

TODO
