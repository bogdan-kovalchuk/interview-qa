---
id: emb-irq-0005
title: "How does interrupt handling work on Cortex-M: NVIC, vector table, priority, and return from ISR?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

The vector table contains the initial SP and handler addresses; the NVIC enables IRQs, tracks pending states, and arbitrates priorities. On ISR entry, Cortex-M automatically stacks caller-saved registers, enters Handler mode, and supports nested interrupts. Returning from an ISR via a special `EXC_RETURN` code restores the context; in an RTOS, this also serves as the context switch hook.[^dou-embedded-interview]

## Detailed explanation

TODO
