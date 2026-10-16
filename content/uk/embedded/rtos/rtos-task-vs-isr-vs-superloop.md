---
id: emb-rtos-0013
title: "Що таке task в RTOS і як він відрізняється від interrupt handler та bare-metal superloop?"
track: embedded
section: rtos
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**RTOS task** має власний stack, priority і scheduler-managed state. Interrupt handler виконується асинхронно в interrupt context, має бути коротким і не поводиться як звичайна task. Bare-metal superloop - один головний цикл без scheduler-а; concurrency там зазвичай будується на flags, ISR і state machines.[^dou-embedded-interview]

## Detailed explanation

TODO
