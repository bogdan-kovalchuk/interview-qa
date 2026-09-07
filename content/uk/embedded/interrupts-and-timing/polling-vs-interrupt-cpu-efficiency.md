---
id: emb-irq-0001
title: "В чому різниця між polling і interrupt?"
description: "Polling витрачає CPU на активне опитування периферії, тоді як interrupt дозволяє периферії сигналізувати подію і звільняє CPU до її настання."
track: embedded
section: interrupts-and-timing
level: junior
type: comparison
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

**Polling** – CPU постійно опитує стан периферії в циклі: `while(!(UART->SR & TXE));`.[^dou-embedded-interview] Просто реалізувати, але CPU зайнятий навіть без подій, тому витрачається потужність і час.

**Interrupt** – периферія сигналізує CPU лише при наявності події. CPU виконує основний код, а при сигналі переривання – зберігає контекст і виконує ISR. Ефективне використання CPU, низька латентність;

Вибір: polling – для простих випадків з передбачуваними подіями; interrupt – коли події нечасті, асинхронні або потрібна низька латентність.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
