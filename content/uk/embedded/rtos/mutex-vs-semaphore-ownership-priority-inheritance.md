---
id: emb-rtos-0009
title: "Чим mutex відрізняється від semaphore у потоках і RTOS tasks?"
description: "<code>mutex</code> має ownership: той task/thread, що lock-нув, має unlock-нути, і часто підтримує priority inheritance (успадкування пріоритету)."
track: embedded
section: rtos
level: middle
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

<code>mutex</code> має ownership: той task/thread, що lock-нув, має unlock-нути, і часто підтримує priority inheritance (успадкування пріоритету). <code>semaphore</code> – лічильник permits/events без такого ownership, тому його можна give/take для ресурсів або сигналізації. Для захисту shared data вибирають mutex; для producer-consumer сигналу або pool count – semaphore.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
