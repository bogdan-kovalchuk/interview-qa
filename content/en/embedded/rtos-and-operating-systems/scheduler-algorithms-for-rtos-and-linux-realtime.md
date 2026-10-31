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
  - source_id: liu-layland-1973
    title: "Liu, Layland: Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment (JACM, 1973)"
    url: https://www.cs.ru.nl/~hooman/DES/liu-layland.pdf
  - source_id: linux-man-sched
    title: "sched(7) - Linux manual page"
    url: https://man7.org/linux/man-pages/man7/sched.7.html
  - source_id: linux-sched-deadline
    title: "The Linux Kernel: Deadline Task Scheduling"
    url: https://docs.kernel.org/scheduler/sched-deadline.html
  - source_id: linux-rt-mutex
    title: "The Linux Kernel: RT-mutex subsystem with PI support"
    url: https://docs.kernel.org/locking/rt-mutex.html
  - source_id: posix-mutexattr-protocol
    title: "POSIX.1-2024: pthread_mutexattr_getprotocol, pthread_mutexattr_setprotocol"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutexattr_getprotocol.html
  - source_id: linux-preempt-rt-theory
    title: "The Linux Kernel: Real-time preemption, theory of operation"
    url: https://docs.kernel.org/core-api/real-time/theory.html
---

## Short answer

In RTOS, **fixed-priority preemptive scheduling** is typically important, sometimes round-robin for tasks of the same priority. For Linux real-time, `SCHED_FIFO`, `SCHED_RR`, priority inheritance, and PREEMPT_RT latency behaviour matter. <span class="warn">A scheduler algorithm must be evaluated together with interrupt latency, locks, and worst-case execution time.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
