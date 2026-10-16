---
id: emb-rtos-0013
title: "What is an RTOS task, and how does it differ from an interrupt handler and a bare-metal superloop?"
track: embedded
section: rtos
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**RTOS task** has its own stack, priority, and scheduler-managed state. An interrupt handler runs asynchronously in interrupt context, must be short, and does not behave like a regular task. A bare-metal superloop is a single main loop without a scheduler; concurrency there is typically built on flags, ISRs, and state machines.[^dou-embedded-interview]

## Detailed explanation

TODO
