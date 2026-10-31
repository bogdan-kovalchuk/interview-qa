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
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Interrupt** is a hardware or software signal that causes the CPU to pause execution of the current code and run a special function – the **ISR (Interrupt Service Routine)**.[^dou-embedded-interview]

Sequence: event, interrupt controller (NVIC), CPU context saving (PC, registers), ISR execution, context restoration, and return to interrupted code.

ISR rules: keep it short and fast; avoid blocking functions; shared variables must be `volatile`; use critical sections (disable/enable IRQ for atomic access).

## Detailed explanation

TODO
