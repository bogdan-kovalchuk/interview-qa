---
id: emb-irq-0009
title: "Як передаються дані між ISR і main loop або RTOS task без race condition?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

Використовують **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores або direct task notification. Shared multi-byte state захищають interrupt disable, mutex у task context або atomic operations, залежно від платформи. <span class="warn">Сам по собі `volatile` не робить операцію atomic і не вирішує race condition.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
