---
id: emb-irq-0005
title: "How does interrupt handling work on Cortex-M with the NVIC, vector table, priorities, and return from an ISR?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

The vector table contains the initial SP and handler addresses; the NVIC enables an IRQ, sets the pending state and selects the highest priority. On ISR entry, Cortex-M automatically stacks part of the registers, switches to handler mode and can perform nested interrupts. Return from ISR uses a special `EXC_RETURN` to restore context; in an RTOS this is also the point for a context switch.[^dou-embedded-interview]

## Detailed explanation

TODO
