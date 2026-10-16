---
id: emb-irq-0009
title: "How is data transferred between an ISR and a main loop or RTOS task without a race condition?"
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

Use **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores or direct task notification. Shared multi-byte state is protected by interrupt disable, mutex in task context or atomic operations, depending on the platform. <span class="warn">`volatile` alone does not make an operation atomic and does not resolve a race condition.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
