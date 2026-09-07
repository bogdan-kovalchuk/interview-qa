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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

**Queue** передає дані між ISR/tasks або tasks, **semaphore** сигналізує подію чи рахує ресурси. **Mutex** захищає shared resource і бажано має priority inheritance. **Event group** зручний для набору flags, коли task чекає одну або кілька умов.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
