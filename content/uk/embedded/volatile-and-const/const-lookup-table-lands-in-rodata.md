---
id: emb-volconst-0025
title: "В яку секцію зазвичай потрапить `const` таблиця?"
description: "У .rodata у Flash, якщо це file-scope або static object і linker script не робить спеціальних винятків."
track: embedded
section: volatile-and-const
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
const uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

У `.rodata` у Flash, якщо це file-scope або static object і linker script не робить спеціальних винятків.

Масив read-only, тому startup code не мусить копіювати його в RAM. Для Cortex-M це економить RAM і час старту. Розмір тут приблизно `256 * 2 = 512` байт, які не займають SRAM.

Правило: великі незмінні таблиці мають бути `const`, інакше вони можуть опинитися у `.data`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
