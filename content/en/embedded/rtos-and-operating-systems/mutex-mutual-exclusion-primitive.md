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
  - source_id: posix-2024-definitions
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 3. Definitions"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: posix-2024-general-concepts
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 4. General Concepts"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html
  - source_id: linux-man-futex7
    title: "Linux manual page: futex(7)"
    url: https://man7.org/linux/man-pages/man7/futex.7.html
  - source_id: linux-mutex-design
    title: "Linux kernel documentation: Generic Mutex Subsystem"
    url: https://docs.kernel.org/locking/mutex-design.html
---

## Short answer

**Mutex** is a synchronization primitive for mutually exclusive access to a shared resource.[^dou-embedded-interview] Only one thread can hold a mutex at a time; other threads must wait.

If the mutex is taken, the thread typically blocks and enters sleep, so CPU is not wasted on busy waiting. This is the key difference from a spinlock, which spins in a loop.

Used to protect shared data such as lists, queues, counters, or state structures; important to acquire and release the mutex in a consistent order to avoid deadlock.

## Detailed explanation

TODO
