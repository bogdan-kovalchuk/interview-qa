---
id: emb-fnptr-0022
title: "Чому function pointer table варто робити `static const`?"
description: "static const робить таблицю file-local і read-only, тому вона може лежати у Flash/.rodata."
track: embedded
section: function-pointers-and-callbacks
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

**`static const`** робить таблицю file-local і read-only, тому вона може лежати у Flash/`.rodata`.

Для MCU це економить RAM і захищає mapping від випадкового runtime overwrite. Якщо table не має змінюватися після build-time, mutable global array – зайвий ризик.

Приклад: `static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
