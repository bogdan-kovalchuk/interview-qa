---
id: emb-irq-0010
title: "Why should an ISR not return a result like an ordinary function, and which patterns replace that?"
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

An ISR is invoked by a hardware/CPU exception mechanism, not by a caller expecting a return value. Results are passed through flags, buffers, queues, semaphores, event bits or deferred work/task notification. **An ISR should signal an event**, while heavy processing belongs in the main loop, a worker task or a bottom half.[^dou-embedded-interview]

## Detailed explanation

TODO
