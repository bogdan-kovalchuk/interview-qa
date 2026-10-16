---
id: emb-rtos-0008
title: "Which synchronization mechanisms are used in POSIX/RTOS, and when should you choose a mutex, semaphore, or condition variable?"
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

`mutex` protects shared state with a single owner in a critical section. `semaphore` counts resources or signals an event between ISR/task in RTOS style, if the API allows it. `condition variable` wakes threads waiting on a predicate under a mutex; it does not store the event by itself.[^dou-embedded-interview]

## Detailed explanation

TODO
