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

Timer clock ділиться через <code>prescaler</code>, після чого <code>counter</code> рахує ticks. <code>auto-reload</code> задає період overflow/update event, а <code>compare</code> генерує подію при збігу counter з каналом. Interrupt або DMA trigger виникає на update/compare/capture, якщо відповідні flags і NVIC enabled.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
