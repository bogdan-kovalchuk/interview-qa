---
id: emb-macros-0008
title: "Чому `static inline` вважають сучасною заміною function-like макросів?"
description: "static inline поєднує internal linkage зі здатністю до inline-розгортання."
track: embedded
section: inline-and-macros
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

**`static inline`** поєднує internal linkage зі здатністю до inline-розгортання.

Він кладеться у header, дає type safety і однократне обчислення аргументів, не створює зайвого external symbol і не конфліктує між translation units (TU – translation unit): кожен TU має власне internal definition або повністю inline-розгорнутий код. Компілятор обирає між розгортанням і викликом за оптимізацією.

Embedded-правило: bit-маніпуляції, дрібні хелпери та обчислення з аргументами роби `static inline` у header, а не макросом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
