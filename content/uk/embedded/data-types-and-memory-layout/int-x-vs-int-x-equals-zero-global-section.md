---
id: emb-dtypes-0031
title: "Чи є різниця між `int x;` і `int x = 0;` оголошеними глобально?"
description: "Обидва дорівнюють нулю при старті, але int x; явно потрапляє у .bss і не витрачає Flash."
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

Поведінково - **НІ**: обидва = 0 при старті. Але є різниця в секції:

`int x;` -> `.bss`: не займає Flash, нуль ставить startup code.
`int x = 0;` -> `.data` (або `.bss` якщо компілятор розпізнає zero-init): значення 0 може зберігатись у Flash.

<span class="warn">Практика</span>: пиши `int x;` без `= 0` для глобальних - явно у `.bss`, не витрачає Flash на нулі.[^embeddedinterviewlab]

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
