---
id: emb-dtypes-0070
title: "Що поверне на 32-bit? `sizeof(struct { char a; char b; int c; })`"
description: "Компілятор додає 2 байти padding перед int, тож struct { char; char; int; } займає 8 байт."
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

**8 байт**.

Layout: `a`@0 (1B) + `b`@1 (1B) + <span class="warn">2B padding</span> + `c`@4 (4B). Trailing padding = 0.

Якби поля у іншому порядку: `struct { char a; int c; char b; }` -> 12 байт (3B padding після `a`, 3B trailing).

Правило: розташовуй поля від більшого alignment до меншого для мінімального sizeof.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
