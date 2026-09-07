---
id: emb-dtypes-0077
title: "Що таке promotion rule і як C обробляє вирази з `char` і `short`?"
description: "Перед арифметикою char і short автоматично промотуються до int, що може дати несподіваний результат для бітових операцій."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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

**Integer promotion** (C §6.3.1.1): перед більшістю арифметичних операцій `char`, `signed char`, `unsigned char`, `short`, `unsigned short` автоматично перетворюються до `int` (або `unsigned int`).

Несподіваний результат: `uint8_t a = 200; uint8_t b = ~a;` - `a` -> `int(200)`, NOT -> `int(0xFFFFFF37 = -201)`, усікається до `uint8_t: 55`.

Завжди розумій promotion до операції.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
