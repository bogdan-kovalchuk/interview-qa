---
id: emb-macros-0037
title: "How do you define access to a memory-mapped register with a macro?"
track: embedded
section: inline-and-macros
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
#define GPIOA_ODR \
  (*(volatile uint32_t *)0x40020014U)
```

## Short answer

**The macro can expand into lvalue access to a memory-mapped register address**, making the expression usable for reads and writes when the address and type match the MCU.

`volatile` requires observable volatile accesses to be preserved according to the C implementation; the cast converts the numeric address to a pointer, and `*` forms an lvalue. The `U` suffix makes the literal unsigned.

Rule: verify that the address, access width, and MCU requirements match the device documentation; C itself does not guarantee that an address is mapped to a register.[^iso-c-n1570]

## Detailed explanation

TODO
