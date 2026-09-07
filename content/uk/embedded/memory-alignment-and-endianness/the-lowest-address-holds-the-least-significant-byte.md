---
id: emb-align-0035
title: "Що виведе цей код на little-endian машині?"
description: "44. На little-endian молодший байт лежить за нижчою адресою, тому p[0] – це LSB 0x44."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
uint32_t w = 0x11223344;
uint8_t *p = (uint8_t*)&w;
printf("%02X", p[0]);
```

## Short answer

**`44`**.

На little-endian молодший байт лежить за нижчою адресою, тому `p[0]` – це LSB `0x44`. На big-endian вивелося б `11`.

Правило: доступ до окремих байтів через `uint8_t*` – типовий спосіб «побачити» endianness; результат залежить від платформи.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
