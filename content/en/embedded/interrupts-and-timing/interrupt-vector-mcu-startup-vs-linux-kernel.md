---
id: emb-irq-0012
title: "What is an interrupt vector, and how does it differ between MCU startup code and the Linux kernel?"
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

On an MCU the **interrupt vector table** usually sits at a fixed address and holds the initial stack pointer and handler addresses. The startup code provides weak default handlers, and the firmware replaces the ISR entries it needs. In Linux, hardware interrupt routing is hidden behind the architecture/kernel IRQ subsystem: a driver registers its handler through the kernel API rather than editing the startup vector table directly.[^dou-embedded-interview]

## Detailed explanation

TODO
