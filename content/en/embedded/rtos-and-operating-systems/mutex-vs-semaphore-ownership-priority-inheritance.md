---
id: emb-rtos-0009
title: "How does a mutex differ from a semaphore in threads and RTOS tasks?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

`mutex` has ownership: the task or thread that locked it must unlock it, and it often supports priority inheritance. `semaphore` is a counter of permits or events without such ownership, so it can be given and taken for resources or signaling. For shared data protection, choose mutex; for producer-consumer signaling or pool count, choose semaphore.[^dou-embedded-interview]

## Detailed explanation

TODO
