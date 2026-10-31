---
id: emb-rtos-0012
title: "How does an RTOS scheduler work, and what do task state, priority, tick, and context switch mean?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: freertos-port-cm4f
    title: "FreeRTOS-Kernel source: portable/GCC/ARM_CM4F/port.c"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/GCC/ARM_CM4F/port.c
  - source_id: freertos-portmacro-cm4f
    title: "FreeRTOS-Kernel source: portable/GCC/ARM_CM4F/portmacro.h"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/GCC/ARM_CM4F/portmacro.h
---

## Short answer

An RTOS scheduler selects the ready task with the highest priority or by policy for equal priority. **Task state** describes ready, running, blocked, or suspended; **tick** provides the system time base; **context switch** saves the current task's registers and restores another. Preemption allows a higher-priority task to preempt a lower one.[^dou-embedded-interview]

## Detailed explanation

TODO
