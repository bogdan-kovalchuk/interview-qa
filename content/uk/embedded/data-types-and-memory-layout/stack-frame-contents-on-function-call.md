---
id: emb-dtypes-0033
title: "Що зберігається у stack frame при виклику функції?"
description: "Stack frame містить збережені регістри, адресу повернення, локальні змінні та вирівнювальний padding."
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

Stack frame містить:
1. **Збережені регістри** (callee-saved per ABI: r4–r11 на ARM);
2. **Адреса повернення** (LR, або push на stack);
3. **Локальні змінні** функції;
4. Padding для вирівнювання (Cortex-M: 8-byte aligned).

При exception (ISR): апаратура автоматично пушить xPSR, PC, LR, R12, R3–R0. Тому глибока вкладеність ISR -> великий stack.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
