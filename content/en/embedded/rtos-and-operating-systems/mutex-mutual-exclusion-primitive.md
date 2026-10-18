---
id: emb-rtos-0002
title: "What is a mutex?"
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

**Mutex** is a synchronization primitive for mutually exclusive access to a shared resource.[^dou-embedded-interview] Only one thread can hold a mutex at a time; other threads must wait.

If the mutex is taken, the thread typically blocks and enters sleep, so CPU is not wasted on busy waiting. This is the key difference from a spinlock, which spins in a loop.

Used to protect shared data such as lists, queues, counters, or state structures; important to acquire and release the mutex in a consistent order to avoid deadlock.

## Detailed explanation

TODO
