---
id: emb-rtos-0010
title: "What is an RTOS, and how does it differ from a general-purpose OS in latency, scheduling, and determinism?"
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

**RTOS** provides bounded interrupt and task latency, priority-based scheduling, and primitives for deterministic embedded tasks. A general-purpose OS optimises throughput, fairness, and multi-user capabilities, so latency can be less predictable. An RTOS does not guarantee "fast always"; it provides controlled worst-case conditions when code and priorities are designed correctly.[^dou-embedded-interview]

## Detailed explanation

TODO
