---
id: emb-cemb-0026
title: "Describe the use of the `volatile` qualifier."
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

It prevents the compiler from caching a variable's value in a register or removing accesses as "dead" – every access performs a real read or write.[^dou-embedded-interview]

It is used when a value can change outside the ordinary execution flow:
- **Peripheral registers**: `volatile uint32_t *GPIOA = (uint32_t *)0x40020000;`
- **A variable modified by an ISR**: `volatile bool flag = false;`
- **Signal handler** or hardware status flag.

For threads, `volatile` by itself <span class="warn">is not synchronization</span>: it does not guarantee atomicity, ordering, or mutual exclusion. For that you need a `mutex`, critical section, or atomics.

## Detailed explanation

TODO
