---
id: emb-dtypes-0073
title: "Як визначити endianness платформи програмно через union?"
description: "Записавши відоме значення у union.word і прочитавши bytes[0], можна визначити little- чи big-endian платформу."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

`union { uint32_t word; uint8_t bytes[4]; } u;
u.word = 0x01020304;
if(u.bytes[0] == 0x04) { /* little-endian */ }`

Little-endian: `bytes[0] = 0x04` (LSB перший). Cortex-M - little-endian за замовчуванням.

Через pointer: `uint32_t x = 1; if(*(char*)&x == 1)` -> little-endian.

Для мережі: `htonl()`/`ntohl()` конвертують між host і network byte order (big-endian).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
