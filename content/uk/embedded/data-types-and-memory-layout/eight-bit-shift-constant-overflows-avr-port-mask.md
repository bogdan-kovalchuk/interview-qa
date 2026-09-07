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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

AVR - 8-bit архітектура, тож `PORTA` - 8-bit регістр, а константа `1<<8 = 256 = 0x100` не вміщається у 8 біт.

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
