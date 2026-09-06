---
id: emb-patterns-0036
title: "Що поверне і чому?"
description: "next == 0 – wraparound на початок буфера."
track: embedded
section: common-code-patterns
level: junior
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

```c
#define RB_SIZE 8
#define RB_MASK (RB_SIZE - 1)
uint16_t head = 7;
uint16_t next = (head + 1) & RB_MASK;
```

**`next == 0`** – wraparound на початок буфера.

`(7 + 1) & 7 = 8 & 0b0111 = 0`. Маска `SIZE-1` = `0b0111` обнуляє біт переповнення, тож індекс «загортається» без `%` чи `if`.

Правило: цей трюк працює тільки якщо `SIZE` – степінь двійки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
