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

На MCU **interrupt vector table** зазвичай лежить за фіксованою адресою і містить initial stack pointer та addresses handlers. Startup code задає weak default handlers, а firmware замінює потрібні ISR. У Linux hardware interrupt routing прихований за architecture/kernel IRQ subsystem: driver реєструє handler через kernel API, а не редагує startup vector table напряму.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
