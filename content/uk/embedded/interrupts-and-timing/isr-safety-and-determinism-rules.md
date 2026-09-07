---
id: emb-irq-0008
title: "Що таке ISR і які правила роблять ISR безпечною та передбачуваною?"
description: "ISR - це interrupt service routine, код який виконується у відповідь на hardware/software interrupt.Вона має бути короткою, deterministic, не blocking…"
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

**ISR** - це interrupt service routine, код який виконується у відповідь на hardware/software interrupt. Вона має бути короткою, deterministic, не blocking, без heap і довгих locks, з мінімальним shared state. Типовий патерн: clear interrupt flag, забрати/покласти мінімальні дані, notify task або main loop.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
