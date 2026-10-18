---
id: emb-cemb-0023
title: "What use cases for volatile do you know?"
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

`volatile` tells the compiler that a value can change outside the ordinary control flow of the current code, so every read and write must actually be performed rather than cached in a register or removed by optimization.

Typical cases: memory-mapped peripheral registers (`volatile uint32_t *reg`), variables modified by an ISR or signal handler, hardware status flags, simple debug and benchmark cases. Importantly, `volatile` <span class="warn">does not make operations atomic</span>, does not guarantee ordering or synchronization, and does not replace a `mutex`, critical section, or `std::atomic`.[^dou-embedded-interview]

## Detailed explanation

TODO
