---
id: emb-align-0043
title: "Що має продемонструвати кандидат у питаннях про alignment і endianness?"
description: "Передбачати padding і перевпорядковувати поля, пояснювати endianness і коректно вживати htonl/ntohl."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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

**Передбачати padding і перевпорядковувати поля, пояснювати endianness і коректно вживати `htonl`/`ntohl`.**

Сильна відповідь також включає: серіалізацію поле за полем замість сирого `struct`, розуміння ціни `packed`, і ризик HardFault на M0 / штрафу на M3/M4 при misaligned доступі.

Правило: говори про явний wire-формат і явний byte order – це маркер досвіду у вбудованих системах.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
