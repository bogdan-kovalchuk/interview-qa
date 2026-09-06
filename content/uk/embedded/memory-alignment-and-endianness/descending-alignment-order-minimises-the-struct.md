---
id: emb-align-0029
title: "Як перевпорядкувати поля `uint64_t, uint8_t, uint32_t, uint8_t`, щоб мінімізувати розмір?"
description: "Від найбільшого alignment до найменшого: uint64_t, uint32_t, uint8_t, uint8_t."
track: embedded
section: memory-alignment-and-endianness
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

**Від найбільшого alignment до найменшого: `uint64_t, uint32_t, uint8_t, uint8_t`.**

Так: `u64`@0(8) + `u32`@8(4) + `u8`@12 + `u8`@13 + 2 tail -> 16 байт. Початковий порядок дав би 24 байти через padding після `uint8_t`.

Правило: «largest first» майже завжди дає мінімальний розмір без packed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
