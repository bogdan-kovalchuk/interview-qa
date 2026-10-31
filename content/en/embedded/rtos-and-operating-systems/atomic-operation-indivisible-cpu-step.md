---
id: emb-rtos-0003
title: "What is an atomic operation?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: cmsis-core-intrinsics
    title: "CMSIS-Core (Cortex-M): Intrinsic Functions for CPU Instructions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__intrinsic__CPU__gr.html
  - source_id: cmsis-core-registers
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
---

## Short answer

**Atomic operation** is an operation that executes indivisibly: other threads or CPUs do not see an intermediate state.[^dou-embedded-interview] For example, an atomic increment does not break down into separate read/modify/write steps for other participants.

Typical examples: atomic load/store, increment/decrement, compare-and-swap (`CAS`). In C++, `std::atomic<T>` is used.

Atomics are needed for counters, flags, and lock-free synchronization; but memory ordering must be understood: atomicity of the variable itself does not always mean correct ordering of access to all related data.

## Detailed explanation

TODO
