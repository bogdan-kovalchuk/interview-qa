---
id: emb-structs-0017
title: "Як безпечніше отримати біти `float` як `uint32_t` у C?"
description: "Через memcpy: uint32_t bits; memcpy(&bits, &f, sizeof bits); memcpy копіює object representation байт-в-байт і не порушує strict aliasing."
track: embedded
section: structs-unions-and-bitfields
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

**Через `memcpy`**:

`uint32_t bits; memcpy(&bits, &f, sizeof bits);`

`memcpy` копіює object representation байт-в-байт і не порушує strict aliasing. Оптимізатор зазвичай перетворює це на один load/store без реального виклику функції, якщо розмір відомий compile-time.

Embedded-правило: для type punning у portable low-level коді `memcpy` часто безпечніший за pointer cast або union trick.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
