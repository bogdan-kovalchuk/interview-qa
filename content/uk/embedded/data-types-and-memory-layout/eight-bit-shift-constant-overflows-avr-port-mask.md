---
id: emb-dtypes-0081
title: "Що не так на 8-bit AVR MCU? `if(!(PORTA & (1<<8)))`"
description: "1<<8 = 256 не вміщається у 8-бітний PORTA, тож маска завжди дає 0 і умова завжди true."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

AVR - 8-bit архітектура. `PORTA` - 8-bit регістр. Константа `1<<8 = 256 = 0x100` - не вміщається у 8 біт.

При обчисленні (int = 16-bit на AVR): `1 << 8 = 0x0100`. `PORTA & 0x0100 = 0` завжди (старший байт PORTA = 0).

Умова <span class="warn">завжди true</span> незалежно від стану PORTA.

Правильно: `if(!(PORTA & (1<<7)))` (максимальний біт - 7 для 8-bit порту).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
