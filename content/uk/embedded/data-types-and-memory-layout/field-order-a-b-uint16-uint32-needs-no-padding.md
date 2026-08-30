---
id: emb-dtypes-0078
title: "Як компілятор розміщує? `struct { uint8_t a; uint8_t b; uint16_t c; uint32_t d; }`"
description: "Цей порядок полів природно заповнює вирівнювальні проміжки, тож struct займає 8 байт без padding."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Оптимальний layout **без padding**:
- `a` @ offset 0 (1B)
- `b` @ offset 1 (1B)
- `c` @ offset 2 (2B, aligned на 2) ✓
- `d` @ offset 4 (4B, aligned на 4) ✓

Разом: **8 байт**, нема padding! Порядок полів підібраний правильно (a, b -> fill to align 2, c fits, d fits).

Загальне правило: поля від **більшого alignment до меншого**. Цей приклад також бездоганний, бо пари `uint8_t` природно заповнюють вирівнювальний gap до `uint16_t`. Перевіряй через `sizeof()` та `offsetof()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
