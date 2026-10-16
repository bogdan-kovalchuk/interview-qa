---
id: emb-cemb-0033
title: "Чому volatile не замінює atomic operations, mutex або critical section?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`volatile` лише каже компілятору не прибирати й не кешувати конкретні accesses. Воно <span class="warn">не робить операцію атомарною</span>, не ставить memory barrier між cores/interrupts і не захищає інваріанти структури даних. Для shared state між task/ISR потрібні atomic operations, interrupt lock, mutex або RTOS primitive залежно від контексту.[^dou-embedded-interview]

## Detailed explanation

TODO
