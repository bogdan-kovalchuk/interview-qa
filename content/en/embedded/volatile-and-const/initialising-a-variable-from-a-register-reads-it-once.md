---
id: emb-volconst-0055
title: "Trap: what is wrong with this register address declaration?"
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
volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;
```

## Short answer

<span class="warn">This creates a separate object and initializes it once with the value read from the register; it is not an alias for the register address.</span>[^iso-c-n1570]

After initialization, `GPIOA_ODR` is a separate object. Writing to it will not write the hardware register.

To access the register, use an lvalue through a pointer or a macro, according to the MCU memory map and compiler rules.[^iso-c-n1570]

## Detailed explanation

TODO
