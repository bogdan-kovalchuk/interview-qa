---
id: emb-fund-0006
title: "What is the difference between a process and a thread?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: posix-2024-definitions
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 3. Definitions"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html
  - source_id: linux-man-pthreads
    title: "Linux manual page: pthreads(7)"
    url: https://man7.org/linux/man-pages/man7/pthreads.7.html
  - source_id: ostep-concurrency-intro
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 26: Concurrency: An Introduction"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf
  - source_id: linux-man-clone
    title: "Linux manual page: clone(2)"
    url: https://man7.org/linux/man-pages/man2/clone.2.html
  - source_id: linux-man-fork
    title: "Linux manual page: fork(2)"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-man-signal
    title: "Linux manual page: signal(7)"
    url: https://man7.org/linux/man-pages/man7/signal.7.html
  - source_id: zephyr-usermode-overview
    title: "Zephyr Project documentation: User Mode Overview"
    url: https://docs.zephyrproject.org/latest/kernel/usermode/overview.html
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**Process** is a separate running program with its own address space, OS resources, file descriptor table and at least one thread.[^dou-embedded-interview] Processes are isolated: a fault in one usually does not corrupt another's memory.

**Thread** is a unit of execution inside a process; threads share memory, heap, globals and descriptors, but each has its own stack, registers and instruction pointer.

Consequence: processes isolate more safely but cost more to create and need IPC; threads are lighter and share data faster, yet need synchronization (`mutex`, `semaphore`, `atomic`) against race conditions.

## Detailed explanation

TODO
