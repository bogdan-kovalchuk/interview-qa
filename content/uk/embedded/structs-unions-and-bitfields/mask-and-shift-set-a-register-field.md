---
id: emb-structs-0025
title: "Як безпечніше встановити поле register без bit-field?"
description: "Типовий патерн: mask + shift."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
#define CTRL_MODE_Pos  4u
#define CTRL_MODE_Msk  (7u << CTRL_MODE_Pos)
```

## Short answer

Типовий патерн: mask + shift.

`reg = (reg & ~CTRL_MODE_Msk) | ((mode << CTRL_MODE_Pos) & CTRL_MODE_Msk);`

Це явно показує, які біти змінюються, не залежить від bit-field layout і збігається з форматом datasheet. Але все ще є read-modify-write, тому для W1C або concurrent hardware bits треба дивитися register semantics.

Правило: masks/shifts більш portable для register definitions, ніж C bit-fields.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
