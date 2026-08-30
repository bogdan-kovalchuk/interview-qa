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
updated: 2026-09-06
content_revision: 1
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? rtos; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

RTOS scheduler вибирає ready task з найвищим priority або за policy для однакового priority.<br><span class="key">Task state</span> описує ready/running/blocked/suspended, <span class="key">tick</span> дає системний time base, а <span class="key">context switch</span> зберігає registers поточної task і відновлює іншу.<br>Preemption дозволяє вищому priority task витіснити нижчий.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
