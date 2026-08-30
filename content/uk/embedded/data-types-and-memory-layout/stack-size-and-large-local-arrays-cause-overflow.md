---
id: emb-dtypes-0042
title: "Які типові розміри stack на Cortex-M і найпоширеніша причина stack overflow?"
description: "Типовий стек Cortex-M - кілька KB, і найчастіша причина переповнення - великі локальні масиви."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Типовий stack на Cortex-M: **1–8 KB** залежно від MCU та linker script.

Причина #1: <span class="warn">великі локальні масиви</span>. Наприклад, `uint8_t buf[2048]` займає 50% стека 4KB! Реальний кейс: automotive sensor crashed після 47 хвилин через 2KB буфер на 4KB стеку при глибокому вкладенні ISR.

Рішення: перенести у `static` / global, `-fstack-usage` для аналізу, MPU guard region.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
