---
id: emb-rtos-0005
title: "What is the difference between a general-purpose OS and a real-time OS?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: linux-man-sched
    title: "Linux manual page: sched(7)"
    url: https://man7.org/linux/man-pages/man7/sched.7.html
  - source_id: linux-preempt-rt-theory
    title: "Linux kernel documentation: Real-time preemption, Theory of operation"
    url: https://docs.kernel.org/core-api/real-time/theory.html
---

## Short answer

**GPOS** (Linux, Windows): optimised for throughput, fairness, and convenience for many processes; latency can be unpredictable without special real-time configuration.[^dou-embedded-interview]

**RTOS** (FreeRTOS, Zephyr, VxWorks): optimised for **determinism** – bounded latency and predictable worst-case response with properly designed priorities, ISRs, and critical sections. In a preemptive RTOS, a ready task with higher priority preempts a lower one.

Key metric – **jitter** (spread of response time). RTOS task examples: motor control, ABS, medical devices.

## Detailed explanation

TODO
