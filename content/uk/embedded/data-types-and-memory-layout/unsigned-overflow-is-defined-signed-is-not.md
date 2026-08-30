---
id: emb-dtypes-0049
title: "Що таке unsigned integer overflow і чим він відрізняється від signed?"
description: "Unsigned overflow визначений стандартом як modular arithmetic, а signed overflow - undefined behavior."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Unsigned overflow - **визначений стандартом** як modular arithmetic по модулю `2^N`:
- `uint8_t: 255 + 1 = 0`
- `uint16_t: 65535 + 1 = 0`

Signed overflow - <span class="warn">undefined behavior</span>: стандарт нічого не гарантує. Компілятор може оптимізувати код припускаючи, що signed overflow не відбувається.

Правило: для arithmetic де можливий wraparound - використовуй unsigned типи.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
