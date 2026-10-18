---
id: emb-rtos-0011
title: "Which scheduler algorithms matter for RTOS and Linux real-time workloads?"
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

In RTOS, **fixed-priority preemptive scheduling** is typically important, sometimes round-robin for tasks of the same priority. For Linux real-time, `SCHED_FIFO`, `SCHED_RR`, priority inheritance, and PREEMPT_RT latency behaviour matter. <span class="warn">A scheduler algorithm must be evaluated together with interrupt latency, locks, and worst-case execution time.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
