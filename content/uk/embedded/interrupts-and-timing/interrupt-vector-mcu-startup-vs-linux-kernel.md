---
id: emb-irq-0012
title: "Що таке interrupt vector і як він відрізняється між MCU startup code та Linux kernel?"
description: "MCU interrupt vector table містить адреси обробників, тоді як Linux приховує маршрутизацію переривань за architecture/kernel IRQ subsystem."
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

На MCU <span class="key">interrupt vector table</span> зазвичай лежить за фіксованою адресою і містить initial stack pointer та addresses handlers.<br>Startup code задає weak default handlers, а firmware замінює потрібні ISR.<br>У Linux hardware interrupt routing прихований за architecture/kernel IRQ subsystem: driver реєструє handler через kernel API, а не редагує startup vector table напряму.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
