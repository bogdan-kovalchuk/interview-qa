---
id: emb-rtos-0004
title: "What is a deadlock?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: ostep-concurrency-bugs
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 32: Common Concurrency Problems"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: linux-spinlocks
    title: "Linux kernel documentation: Locking lessons (spinlocks)"
    url: https://docs.kernel.org/locking/spinlocks.html
  - source_id: linux-lockdep-design
    title: "Linux kernel documentation: Runtime locking correctness validator"
    url: https://docs.kernel.org/locking/lockdep-design.html
---

## Short answer

**Deadlock** is a situation where two or more threads mutually wait for each other's resources and none can proceed.[^dou-embedded-interview]

Example: Thread A took `m1` and waits for `m2`, while Thread B took `m2` and waits for `m1`. Both are blocked forever.

Prevention: fixed order of acquiring locks, short critical sections, timeout, lock hierarchy, avoiding nested locks, or using higher-level primitives.

## Detailed explanation

TODO
