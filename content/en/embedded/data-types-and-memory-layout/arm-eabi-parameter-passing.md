---
id: emb-cemb-0043
title: "How are function parameters passed under EABI on ARM Cortex-M?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Under ARM EABI/AAPCS the first simple integer/pointer arguments are typically passed in `r0-r3`, and the result in `r0` or `r0:r1`. Additional arguments and parts of large aggregate objects go through the stack with proper alignment. Registers `r4-r11` are callee-saved, and `r0-r3,r12,lr` are caller-saved in the normal calling convention.[^dou-embedded-interview]

## Detailed explanation

TODO
