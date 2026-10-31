---
id: emb-rtos-0001
title: "What is a race condition?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: ostep-concurrency-intro
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 26: Concurrency: An Introduction"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf
  - source_id: ostep-concurrency-bugs
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 32: Common Concurrency Problems"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: posix-2024-general-concepts
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 4. General Concepts"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html
---

## Short answer

**Race condition** is a situation where the outcome depends on the execution order of threads, processes, or ISRs.[^dou-embedded-interview] If the order changes, the program may sometimes work correctly and sometimes produce an error.

Classic example: `counter++` is not a single atomic action but a sequence of read, modify, write; if two threads read the old value simultaneously, one increment can be lost.

Protection: `mutex`, spinlock, atomic operations, critical section, or briefly disabling interrupts in embedded code.

## Detailed explanation

TODO
