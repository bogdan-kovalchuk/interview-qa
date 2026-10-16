---
id: emb-rtos-0003
title: "What is an atomic operation?"
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

**Atomic operation** is an operation that executes indivisibly: other threads or CPUs do not see an intermediate state.[^dou-embedded-interview] For example, an atomic increment does not break down into separate read/modify/write steps for other participants.

Typical examples: atomic load/store, increment/decrement, compare-and-swap (`CAS`). In C++, `std::atomic<T>` is used.

Atomics are needed for counters, flags, and lock-free synchronization; but memory ordering must be understood: atomicity of the variable itself does not always mean correct ordering of access to all related data.

## Detailed explanation

TODO
