---
id: emb-cemb-0023
title: "Які варіанти використання volatile знаєте?"
track: embedded
section: volatile-and-const
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`volatile` каже компілятору, що значення може змінитися поза звичайним контролем поточного коду, тому кожне читання/запис треба реально виконувати, а не кешувати в регістрі чи прибирати оптимізацією.

Типові випадки: memory-mapped регістри периферії (`volatile uint32_t *reg`), змінні, які змінює ISR або signal handler, hardware status flags, прості debug/benchmark випадки. Важливо: `volatile` <span class="warn">не робить операції атомарними</span>, не гарантує ordering/synchronization і не замінює `mutex`, critical section або `std::atomic`.[^dou-embedded-interview]

## Detailed explanation

TODO
