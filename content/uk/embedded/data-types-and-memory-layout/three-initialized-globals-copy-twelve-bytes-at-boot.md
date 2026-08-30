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
