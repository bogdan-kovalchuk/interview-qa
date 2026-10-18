---
id: emb-cemb-0033
title: "Why does volatile not replace atomic operations, mutexes, or critical sections?"
track: embedded
section: volatile-and-const
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`volatile` only tells the compiler not to remove or cache specific accesses. It <span class="warn">does not make the operation atomic</span>, does not place a memory barrier between cores/interrupts, and does not protect data structure invariants. For shared state between tasks/ISRs, atomic operations, interrupt locks, mutexes, or RTOS primitives are needed depending on the context.[^dou-embedded-interview]

## Detailed explanation

TODO
