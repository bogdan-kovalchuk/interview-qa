---
id: emb-dtypes-0019
title: "Що таке little-endian і big-endian? Як Cortex-M зберігає `0x12345678`?"
description: "Little-endian зберігає молодший байт за нижчою адресою; Cortex-M за замовчуванням little-endian."
track: embedded
section: data-types-and-memory-layout
level: junior
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

**Endianness** - порядок байтів багатобайтових типів у пам'яті.

**Little-endian**: LSB (молодший байт) за нижчою адресою. Cortex-M за замовчуванням little-endian: `0x12345678` у пам'яті -> `[78][56][34][12]` (адреса зростає ->).

**Big-endian**: MSB перший. Використовується у мережевих протоколах (TCP/IP, MODBUS); Для конвертації: `htonl()` / `ntohl()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
