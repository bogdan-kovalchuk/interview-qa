---
id: emb-memlink-0016
title: "What is a linker script, and what errors in it can break firmware startup?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: gcc-arm-options
    title: "GCC: ARM Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
---

## Short answer

A **linker script** describes Flash/RAM regions, the entry point, sections, the vector table, and symbols for startup. Typical errors: wrong vector table address, overlapping `.data/.bss/heap/stack`, unexported `_sidata/_sdata/_edata/_sbss/_ebss`, incorrect RAM origin/length. <span class="warn">Such errors often manifest as a reset loop or a HardFault before main</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
