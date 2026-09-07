---
id: emb-align-0032
title: "Як правильно надіслати дані між двома різними MCU?"
description: "Визначити явний wire-формат і серіалізувати поле за полем з явним byte order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 3
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

**Визначити явний wire-формат і серіалізувати поле за полем з явним byte order.**

Це канонічна відповідь на інтерв'ю: жодних сирих `memcpy` структур, бо padding і endianness відрізняються. Кожне багатобайтове поле – через `htonl`/`htons` у фіксований offset.

Правило: документований wire-формат + field-by-field (де)серіалізація = портативність між будь-якими платформами.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
