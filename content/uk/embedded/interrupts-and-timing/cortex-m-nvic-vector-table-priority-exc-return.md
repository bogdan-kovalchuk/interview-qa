---
id: emb-irq-0005
title: "Як працює interrupt handling на Cortex-M: NVIC, vector table, priority і return from ISR?"
description: "Vector table містить initial SP і addresses handlers; NVIC enable-ить IRQ, виставляє pending state і вибирає найвищий priority."
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? interrupts-and-timing; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Vector table містить initial SP і addresses handlers; NVIC enable-ить IRQ, виставляє pending state і вибирає найвищий priority. При вході в ISR Cortex-M автоматично stacking-ить частину registers, переходить у handler mode і може робити nested interrupts. Return from ISR через спеціальне <code>EXC_RETURN</code> відновлює context; у RTOS це також точка для context switch.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

