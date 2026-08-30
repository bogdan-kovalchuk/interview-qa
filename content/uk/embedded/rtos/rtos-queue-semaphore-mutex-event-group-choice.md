---
id: emb-rtos-0014
title: "Які synchronization primitives є в RTOS і коли використовувати queue, semaphore, mutex або event group?"
description: "Queue передає дані, semaphore сигналізує подію, mutex захищає ресурс, а event group об'єднує умови очікування."
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

<span class="key">Queue</span> передає дані між ISR/tasks або tasks, <span class="key">semaphore</span> сигналізує подію чи рахує ресурси.<br><span class="key">Mutex</span> захищає shared resource і бажано має priority inheritance.<br><span class="key">Event group</span> зручний для набору flags, коли task чекає одну або кілька умов.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
