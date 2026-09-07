---
id: emb-irq-0010
title: "Чому ISR не має повертати результат як звичайна функція і які патерни використовують замість цього?"
description: "ISR викликається hardware/CPU exception механізмом, а не caller-ом, який чекає return value.Результат передають через flags, buffers, queues, semaphor…"
track: embedded
section: interrupts-and-timing
level: senior
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

ISR викликається hardware/CPU exception механізмом, а не caller-ом, який чекає return value. Результат передають через flags, buffers, queues, semaphores, event bits або deferred work/task notification. **ISR має сигналізувати подію**, а важку обробку виконувати у main loop, worker task або bottom half.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
