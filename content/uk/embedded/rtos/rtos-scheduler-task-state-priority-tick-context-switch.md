---
id: emb-rtos-0012
title: "Як працює RTOS scheduler і що означають task state, priority, tick і context switch?"
description: "RTOS scheduler обирає готову task, а task state, priority, tick і context switch описують її планування та перемикання."
track: embedded
section: rtos
level: senior
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

RTOS scheduler вибирає ready task з найвищим priority або за policy для однакового priority. **Task state** описує ready/running/blocked/suspended, **tick** дає системний time base, а **context switch** зберігає registers поточної task і відновлює іншу. Preemption дозволяє вищому priority task витіснити нижчий.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
