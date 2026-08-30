---
id: emb-irq-0011
title: "Як працюють hardware timers у режимах PWM, input capture, output compare і one-pulse?"
description: "У PWM timer рахує період і порівнює counter з duty value, керуючи output pin.Input capture зберігає counter на edge для вимірювання часу, а output com…"
track: embedded
section: interrupts-and-timing
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
---

## Short answer

У <span class="key">PWM</span> timer рахує період і порівнює counter з duty value, керуючи output pin.<br><span class="key">Input capture</span> зберігає counter на edge для вимірювання часу, а <span class="key">output compare</span> генерує подію/зміну pin при match.<br><span class="key">One-pulse</span> запускає одноразовий імпульс заданої тривалості після trigger.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
