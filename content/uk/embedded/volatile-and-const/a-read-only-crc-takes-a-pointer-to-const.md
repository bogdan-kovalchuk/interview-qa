---
id: emb-volconst-0051
title: "Яке оголошення краще для функції CRC, яка лише читає дані?"
description: "Краще: uint32_t crc32(const uint8_t data, size_t len); CRC не змінює buffer, тому pointer має бути to const data."
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
uint32_t crc32(? data, size_t len);
```

## Short answer

Краще: `uint32_t crc32(const uint8_t *data, size_t len);`

CRC не змінює buffer, тому pointer має бути to const data. Це дозволяє рахувати CRC для RAM buffer, Flash table, firmware image slice або string literal без втрати type safety.

Embedded-правило: read-only algorithm input має бути `const`; це економить RAM у caller-а і зменшує ризик випадкових записів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
