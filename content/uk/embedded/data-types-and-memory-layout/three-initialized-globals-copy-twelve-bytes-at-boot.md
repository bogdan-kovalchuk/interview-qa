---
id: emb-dtypes-0085
title: "Скільки байт скопіює startup code для (глобальні)? `int a=1; int b=2; int c=3;`"
description: "Усі три - ініціалізовані глобальні у .data, тож startup code копіює 12 байт (3 * sizeof(int)) з Flash у RAM."
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

**12 байт** (3 × `sizeof(int)` = 3 × 4).

Всі три - ініціалізовані глобальні -> `.data`. Startup code копіює весь блок `.data` з Flash у RAM одним memcpy-подібним циклом.

Початкові значення у Flash (little-endian): `{0x01,0x00,0x00,0x00, 0x02,0x00,0x00,0x00, 0x03,0x00,0x00,0x00}` -> копіюються у RAM.

Якби `int a=0; int b=0; int c=0;` -> компілятор може перенести у `.bss` (0B Flash).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
