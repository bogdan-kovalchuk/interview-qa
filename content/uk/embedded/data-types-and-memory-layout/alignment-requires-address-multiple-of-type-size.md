---
id: emb-dtypes-0012
title: "Що таке alignment і чому CPU вимагає вирівнювання даних?"
description: "Alignment вимагає, щоб дані лежали за адресою, кратною своєму розміру, бо так CPU читає пам'ять."
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

Alignment - вимога щоб дані певного типу знаходились за адресою, **кратною їх розміру**. Наприклад, `uint32_t` (4B) -> адреса кратна 4.

CPU читає пам'ять word-aligned шматками. Misaligned access:
- Cortex-M0/M0+: <span class="warn">HardFault</span>
- Cortex-M3/M4: штраф продуктивності або fault залежно від налаштувань CCR.UNALIGN_TRP

`_Alignof(T)` повертає вимогу вирівнювання типу T.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
