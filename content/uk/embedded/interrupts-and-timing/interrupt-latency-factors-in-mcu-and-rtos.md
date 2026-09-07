---
id: emb-irq-0006
title: "Що таке interrupt latency і які фактори її збільшують у MCU або RTOS?"
description: "Interrupt latency – час від hardware event до виконання першої корисної інструкції ISR."
track: embedded
section: interrupts-and-timing
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Авторитетне джерело рівня секції для понять розділу interrupts-and-timing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Interrupt latency – час від hardware event до виконання першої корисної інструкції ISR. Її збільшують disabled interrupts, вищі priority ISR, довгі critical sections, flash wait states, cache misses, bus contention, FPU stacking і RTOS interrupt masking. Для зменшення latency ISR має бути короткою, а важку роботу треба переносити в task/deferred handler.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

