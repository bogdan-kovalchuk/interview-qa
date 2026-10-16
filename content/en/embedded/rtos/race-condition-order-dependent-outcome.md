---
id: emb-rtos-0001
title: "What is a race condition?"
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

**Race condition** is a situation where the outcome depends on the execution order of threads, processes, or ISRs.[^dou-embedded-interview] If the order changes, the program may sometimes work correctly and sometimes produce an error.

Classic example: `counter++` is not a single atomic action but a sequence of read, modify, write; if two threads read the old value simultaneously, one increment can be lost.

Protection: `mutex`, spinlock, atomic operations, critical section, or briefly disabling interrupts in embedded code.

## Detailed explanation

TODO
