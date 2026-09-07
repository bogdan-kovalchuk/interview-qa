---
id: emb-rtos-0013
title: "Що таке task в RTOS і як він відрізняється від interrupt handler та bare-metal superloop?"
description: "RTOS task має власний stack і priority, interrupt handler працює в interrupt context, а bare-metal superloop є головним циклом без scheduler-а."
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

**RTOS task** має власний stack, priority і scheduler-managed state. Interrupt handler виконується асинхронно в interrupt context, має бути коротким і не поводиться як звичайна task. Bare-metal superloop - один головний цикл без scheduler-а; concurrency там зазвичай будується на flags, ISR і state machines.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
