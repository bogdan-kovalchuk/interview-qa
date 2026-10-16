---
id: emb-dtypes-0033
title: "What does a stack frame hold on a function call?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Stack frame contents depend on the ABI, compiler, and optimization: it may contain saved registers, a return address, local data, and padding, but there is no universal fixed list. On Cortex-M, exception entry automatically stacks a basic frame containing R0–R3, R12, LR, PC, and xPSR; cores with an FPU can use an extended frame and lazy stacking.[^armv7m]

## Detailed explanation

TODO
