---
id: emb-irq-0004
title: "Як працює таймер MCU: counter, prescaler, auto-reload, compare і interrupt event?"
description: "Таймер ділить clock через prescaler, рахує ticks у counter і створює update або compare events для interrupt чи DMA."
track: embedded
section: interrupts-and-timing
level: middle
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Авторитетне джерело рівня секції для понять розділу interrupts-and-timing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Timer clock ділиться через `prescaler`, після чого `counter` рахує ticks. `auto-reload` задає період overflow/update event, а `compare` генерує подію при збігу counter з каналом. Interrupt або DMA trigger виникає на update/compare/capture, якщо відповідні flags і NVIC enabled.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
