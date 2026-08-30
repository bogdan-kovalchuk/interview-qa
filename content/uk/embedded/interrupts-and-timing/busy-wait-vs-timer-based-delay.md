---
id: emb-irq-0007
title: "Як реалізований delay у firmware і чому busy-wait delay часто гірший за timer-based підхід?"
description: "Delay може бути busy loop, CPU cycle counter, SysTick, hardware timer або RTOS sleep.Timer-based delay краще зберігає CPU time, дозволяє sleep/power s…"
track: embedded
section: interrupts-and-timing
level: senior
type: pitfall
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
---

## Short answer

Delay може бути busy loop, CPU cycle counter, SysTick, hardware timer або RTOS sleep.<br><span class="key">Timer-based delay</span> краще зберігає CPU time, дозволяє sleep/power saving і не ламається від зміни clock чи optimization.<br><span class="warn">Busy-wait блокує main loop/task і погано масштабується для ISR-driven або RTOS firmware.</span>[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
