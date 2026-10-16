---
id: emb-structs-0008
title: "What does this code check?"
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

## Question code

```c
_Static_assert(offsetof(GPIO_TypeDef, ODR) == 0x14,
               "bad GPIO layout");
```

## Short answer

At compile time, it checks that the `ODR` field in `GPIO_TypeDef` has offset `0x14`.

For a peripheral struct overlay this is critical: if preceding fields or reserved gaps are incorrect, `GPIOA->ODR` accesses a different address. On Cortex-M this can mean the wrong peripheral, a silent bug, or a fault.

This requires a correct type definition and `<stddef.h>` for `offsetof`; the assertion checks the compiled layout, but does not confirm the peripheral base address or the accuracy of the hardware manual.[^iso-c-n1570]

## Detailed explanation

TODO
