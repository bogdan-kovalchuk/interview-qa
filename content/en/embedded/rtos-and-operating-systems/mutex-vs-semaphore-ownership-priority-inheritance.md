---
id: emb-rtos-0009
title: "How does a mutex differ from a semaphore in threads and RTOS tasks?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: posix-pthread-mutexattr-protocol
    title: "POSIX.1-2024: pthread_mutexattr_getprotocol, pthread_mutexattr_setprotocol"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutexattr_getprotocol.html
  - source_id: posix-sem-post
    title: "POSIX.1-2024: sem_post"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html
  - source_id: linux-mutex-design
    title: "Linux kernel: Generic Mutex Subsystem"
    url: https://docs.kernel.org/locking/mutex-design.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
---

## Short answer

`mutex` has ownership: the task or thread that locked it must unlock it, and it often supports priority inheritance. `semaphore` is a counter of permits or events without such ownership, so it can be given and taken for resources or signaling. For shared data protection, choose mutex; for producer-consumer signaling or pool count, choose semaphore.[^dou-embedded-interview]

## Detailed explanation

TODO
