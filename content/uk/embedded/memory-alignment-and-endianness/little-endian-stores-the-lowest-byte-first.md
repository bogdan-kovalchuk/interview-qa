---
id: emb-align-0012
title: "Як у пам'яті little-endian машини ляже `0xDEADBEEF`?"
description: "EF BE AD DE (від нижчої адреси до вищої)."
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

**`EF BE AD DE`** (від нижчої адреси до вищої).

Little-endian кладе молодший байт першим: `0xEF` @0, `0xBE` @1, `0xAD` @2, `0xDE` @3.

Правило: щоб «прочитати» LE-дамп як число, читай байти справа наліво.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
