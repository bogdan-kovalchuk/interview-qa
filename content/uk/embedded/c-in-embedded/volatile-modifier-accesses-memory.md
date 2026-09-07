---
id: emb-cemb-0026
title: "Опишіть використання модифікатора `volatile`."
description: "`volatile` змушує компілятор виконувати читання і записи, які можуть змінюватися поза звичайним потоком виконання."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Забороняє компілятору кешувати значення змінної в регістрі або прибирати доступ як "зайвий" – при кожному зверненні виконується реальне читання/запис.[^dou-embedded-interview]

Використовується коли значення може змінитися поза звичайним потоком виконання:
- **Регістри периферії**: `volatile uint32_t *GPIOA = (uint32_t *)0x40020000;`
- **Змінна, яку змінює ISR**: `volatile bool flag = false;`
- **Signal handler** або hardware status flag.

Для потоків сам по собі `volatile` <span class="warn">не є синхронізацією</span>: не гарантує atomicity, ordering або mutual exclusion. Для цього потрібні `mutex`, critical section або atomics.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
