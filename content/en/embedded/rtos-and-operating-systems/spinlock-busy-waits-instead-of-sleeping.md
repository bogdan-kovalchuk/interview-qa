---
id: emb-rtos-0006
title: "What is a spinlock?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: posix-pthread-spin-lock
    title: "POSIX.1-2024: pthread_spin_lock, pthread_spin_trylock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_spin_lock.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-kernel-locking-guide
    title: "Linux kernel: Unreliable Guide To Locking"
    url: https://docs.kernel.org/kernel-hacking/locking.html
  - source_id: linux-locking-lessons
    title: "Linux kernel: Locking lessons (spin locks)"
    url: https://docs.kernel.org/locking/spinlocks.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
  - source_id: linux-man-sched
    title: "Linux manual page: sched(7)"
    url: https://man7.org/linux/man-pages/man7/sched.7.html
---

## Short answer

**Spinlock** is a synchronization primitive where a thread that cannot acquire the lock **spins in a loop**, checking availability instead of sleeping.[^dou-embedded-interview]

Advantage: low latency when the wait is very short. In kernel space spinlocks are used where sleeping is forbidden and, depending on lock type and context, may disable preemption or IRQs; in user space a spinlock is just busy waiting.

Rule: <span class="warn">you must not sleep while holding a spinlock</span>; for a long critical section or code that may block, prefer a mutex.

## Detailed explanation

TODO
