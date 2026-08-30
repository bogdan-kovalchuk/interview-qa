---
id: emb-dtypes-0050
title: "Що означає? `__attribute__((section(\".ccmram\"))) uint32_t fast_buf[256];`"
description: "Атрибут section розміщує масив у .ccmram - швидку RAM без wait states для критичних за часом буферів."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

Розміщує масив у секцію **.ccmram** (Core Coupled Memory RAM) на STM32 F4/F7 - спеціальна RAM підключена безпосередньо до CPU без bus matrix.

Забезпечує **zero-wait-state** доступ: ідеально для time-critical буферів, lookup tables, стека ISR.

Потрібно: 1. Визначити секцію у linker script (`MEMORY { CCMRAM ... }`); 2. Ініціалізувати у startup code. Не доступна DMA на деяких MCU - перевіряй reference manual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
