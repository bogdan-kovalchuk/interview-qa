---
id: emb-patterns-0019
title: "Чому `ERR_OK` завжди дорівнює 0?"
description: "Щоб 0 означав успіх, а будь-яке ненульове значення – помилку (truthiness)."
track: embedded
section: common-code-patterns
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

**Щоб `0` означав успіх, а будь-яке ненульове значення – помилку** (truthiness).

Тоді `if (result) { handle_error(); }` і `if (sensor_read(...) != ERR_OK)` працюють природно. Це типова конвенція HAL (hardware abstraction layer) і багатьох POSIX-подібних API (application programming interface): 0 = success, non-zero/negative value = error.

Правило: у enum помилок `ERR_OK = 0` на першому місці; реальні коди – ненульові.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
