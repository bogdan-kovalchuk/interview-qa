---
id: emb-rtos-0001
title: "Що таке race condition?"
description: "Race condition – ситуація, коли результат залежить від порядку виконання потоків, процесів або ISR, і захищається mutex, atomics чи critical section."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу rtos; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Race condition** – ситуація, коли результат залежить від порядку виконання потоків, процесів або ISR.[^dou-embedded-interview] Якщо порядок змінюється, програма може іноді працювати правильно, а іноді давати помилку.

Класичний приклад: `counter++`. Це не одна атомарна дія, а послідовність read, modify, write. Якщо два потоки одночасно читають старе значення, один інкремент може загубитися.

Захист: `mutex`, spinlock, atomic operations, critical section або вимкнення interrupt-ів на короткий час в embedded-коді.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
