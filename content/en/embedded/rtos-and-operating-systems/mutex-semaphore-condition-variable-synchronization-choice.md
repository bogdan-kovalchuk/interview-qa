---
id: emb-rtos-0008
title: "Which synchronization mechanisms are used in POSIX/RTOS, and when should you choose a mutex, semaphore, or condition variable?"
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
  - source_id: posix-sem-post
    title: "POSIX.1-2024: sem_post"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html
  - source_id: posix-pthread-cond-wait
    title: "POSIX.1-2024: pthread_cond_clockwait, pthread_cond_timedwait, pthread_cond_wait"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_wait.html
  - source_id: posix-pthread-cond-signal
    title: "POSIX.1-2024: pthread_cond_broadcast, pthread_cond_signal"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_signal.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
---

## Short answer

`mutex` protects shared state with a single owner in a critical section. `semaphore` counts resources or signals an event between ISR/task in RTOS style, if the API allows it. `condition variable` wakes threads waiting on a predicate under a mutex; it does not store the event by itself.[^dou-embedded-interview]

## Detailed explanation

TODO
