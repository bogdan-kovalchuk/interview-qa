---
id: emb-irq-0009
title: "Як передаються дані між ISR і main loop або RTOS task без race condition?"
description: "Використовують volatile/atomic flags, lock-free ring buffers, critical sections, RTOS queues/semaphores або direct task notification.Shared multi-byte…"
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

Використовують **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores або direct task notification. Shared multi-byte state захищають interrupt disable, mutex у task context або atomic operations, залежно від платформи. <span class="warn">Сам по собі `volatile` не робить операцію atomic і не вирішує race condition.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
