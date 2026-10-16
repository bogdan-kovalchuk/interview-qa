---
id: emb-structs-0026
title: "Trap: what is wrong with a read-modify-write on a status register?"
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
STATUS.bits.error = 0;
```

## Short answer

<span class="warn">The compiler may generate a read-modify-write of the entire register.</span>

If STATUS has read-to-clear bits or write-one-to-clear bits, writing a single bit-field may inadvertently clear or modify other flags. For hardware registers, semantics matter more than C-level convenience.

Defence: use the documented clear register or write the exact mask, for example `STATUS = ERROR_Msk;` for W1C, if the manual requires it.[^stm32-w1c-manual]

## Detailed explanation

TODO
