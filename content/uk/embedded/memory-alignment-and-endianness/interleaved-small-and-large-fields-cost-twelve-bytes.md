---
id: emb-align-0004
title: "Який `sizeof` матиме на 32-bit MCU?"
description: "12 байт. Layout: flags@0 (1B) -> 3B padding -> timestamp@4 (4B) -> sensor_id@8 (1B) -> 3B trailing padding (щоб розмір був кратний 4)."
track: embedded
section: memory-alignment-and-endianness
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
typedef struct {
  uint8_t  flags;
  uint32_t timestamp;
  uint8_t  sensor_id;
} bad_t;
```

## Short answer

**12 байт.**

Layout: `flags`@0 (1B) -> <span class="warn">3B padding</span> -> `timestamp`@4 (4B) -> `sensor_id`@8 (1B) -> <span class="warn">3B trailing padding</span> (щоб розмір був кратний 4).

Захист: перевпорядкуй поля від більшого alignment до меншого – тоді буде 8 байт.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
