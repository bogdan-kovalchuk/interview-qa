---
id: emb-dtypes-0023
title: "Який layout пам'яті матиме? `union { uint32_t word; uint8_t bytes[4]; };`"
description: "Усі поля union накладаються на одну й ту саму пам'ять розміром з найбільше поле."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Всі поля займають **одну і ту саму область** пам'яті. Розмір = `max(sizeof(uint32_t), sizeof(uint8_t[4])) = 4` байти.

На little-endian (Cortex-M): якщо `word = 0x12345678`, то:
`bytes[0] = 0x78` (LSB), `bytes[1] = 0x56`, `bytes[2] = 0x34`, `bytes[3] = 0x12` (MSB).

Використання: перевірка endianness, byte-level serialization, IEEE 754 bit inspection.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
