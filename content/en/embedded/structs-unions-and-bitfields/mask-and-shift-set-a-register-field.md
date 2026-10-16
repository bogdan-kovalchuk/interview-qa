---
id: emb-structs-0025
title: "What is the safer way to set a register field without a bit-field?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
---

## Question code

```c
#define CTRL_MODE_Pos  4u
#define CTRL_MODE_Msk  (7u << CTRL_MODE_Pos)
```

## Short answer

Typical pattern: mask + shift.

`reg = (reg & ~CTRL_MODE_Msk) | ((mode << CTRL_MODE_Pos) & CTRL_MODE_Msk);`

This explicitly shows which bits are being changed, does not depend on bit-field layout, and matches the datasheet format. But there is still a read-modify-write, so for W1C or concurrent hardware bits you need to check the register semantics.

Rule: masks/shifts are more portable for register definitions than C bit-fields.[^iso-c-n1570]

## Detailed explanation

TODO
