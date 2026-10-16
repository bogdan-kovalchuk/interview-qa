---
id: emb-rtos-0014
title: "Which synchronization primitives exist in an RTOS, and when should you use a queue, semaphore, mutex, or event group?"
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

**Queue** transfers data between ISR/tasks or tasks; **semaphore** signals an event or counts resources. **Mutex** protects a shared resource and preferably has priority inheritance. **Event group** is convenient for a set of flags when a task waits on one or more conditions.[^dou-embedded-interview]

## Detailed explanation

TODO
