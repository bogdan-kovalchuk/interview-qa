---
id: emb-dtypes-0018
title: "Намалюйте memory layout без packing `struct { uint8_t a; uint32_t b; uint8_t c; }`"
description: "Компілятор вставляє padding між uint8_t і uint32_t полями, тож struct займає 12, а не 6 байт."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

`a` @ offset 0 (1B) -> <span class="warn">3B padding</span> -> `b` @ offset 4 (4B) -> `c` @ offset 8 (1B) -> <span class="warn">3B trailing padding</span>

Разом: **12 байт**. Trailing padding забезпечує правильне вирівнювання в масиві: `arr[1].b` також буде на адресі кратній 4.

Оптимізація: `struct { uint32_t b; uint8_t a; uint8_t c; }` -> 8 байт без внутрішнього padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
