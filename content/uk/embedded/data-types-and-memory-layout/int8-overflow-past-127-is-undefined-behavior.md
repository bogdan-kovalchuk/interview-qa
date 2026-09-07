---
id: emb-dtypes-0020
title: "Що відбудеться? `int8_t x = 127; x++;`"
description: "Переповнення int8_t за 127 - undefined behavior за стандартом C, хоча на практиці часто wrap-ає у -128."
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

<span class="warn">Signed integer overflow -> undefined behavior</span> за стандартом C (§6.5).

На практиці (two's complement, більшість компіляторів): `127 + 1 = -128` (wrap). Але стандарт не гарантує цієї поведінки - компілятор може оптимізувати код припускаючи, що overflow не відбувається.

Для визначеного wraparound: використовуй `uint8_t`. Для перевірки: `if(x < INT8_MAX) x++;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
