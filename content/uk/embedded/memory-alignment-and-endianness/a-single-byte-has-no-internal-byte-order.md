---
id: emb-align-0040
title: "Чому однобайтові поля (`uint8_t`) не потребують byte swap при серіалізації?"
description: "Endianness стосується лише порядку байтів усередині багатобайтового значення."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

**Endianness стосується лише порядку байтів усередині багатобайтового значення.**

Один байт не має «внутрішнього порядку», тому `uint8_t` однаковий на LE і BE – його кладуть у буфер як є.

Правило: `htonl`/`htons` застосовуй до 16/32/64-бітних полів; для `uint8_t` і масивів байтів конвертація не потрібна.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
