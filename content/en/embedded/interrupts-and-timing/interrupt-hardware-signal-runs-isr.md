---
id: emb-irq-0003
title: "What is an interrupt?"
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

**Interrupt** is a hardware or software signal that forces the CPU to suspend the current code and execute a special function – an **ISR (Interrupt Service Routine)**.[^dou-embedded-interview]

Sequence: an event occurs, then the interrupt controller (NVIC), then the CPU saves context (PC, registers), executes the ISR, restores context and returns to the main code.

ISR rules: keep it short and fast; do not use blocking functions; shared variables must be `volatile`; critical sections (disable/enable IRQ for atomic access) may be needed.

## Detailed explanation

TODO
