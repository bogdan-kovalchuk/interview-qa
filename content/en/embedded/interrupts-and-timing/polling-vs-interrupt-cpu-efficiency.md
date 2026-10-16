---
id: emb-irq-0001
title: "What is the difference between polling and interrupts?"
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

**Polling** – the CPU continuously reads peripheral state in a loop: `while(!(UART->SR & TXE));`.[^dou-embedded-interview] Simple to implement, but the CPU stays busy even without events, wasting power and time.

**Interrupt** – the peripheral signals the CPU only when an event occurs. The CPU runs the main code, and on an interrupt request it saves context and executes the ISR; efficient CPU use, low latency.

Choice: polling – for simple cases with predictable events; interrupt – when events are infrequent, asynchronous or low latency is required.

## Detailed explanation

TODO
