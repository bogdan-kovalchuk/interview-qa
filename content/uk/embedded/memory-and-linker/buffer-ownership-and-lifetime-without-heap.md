---
id: emb-memlink-0014
title: "Як реалізувати ownership і lifetime для буферів без heap у embedded C?"
description: "Практичне питання про embedded-розробку та її обмеження."
track: embedded
section: memory-and-linker
level: middle
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Виділити буфери статично або в pool і явно визначити owner: driver, task, queue чи caller. Передавати не «сирий ресурс назавжди», а handle або descriptor зі станом `free/in_use/done`. Для ISR/DMA добре працюють ring buffer, double buffer і callback/queue, де lifetime завершується після явного release.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

