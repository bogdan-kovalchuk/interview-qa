---
id: emb-fnptr-0050
title: "Чому callback API має документувати execution context?"
description: "Бо той самий callback type може викликатися з ISR, task, main loop або driver lock context."
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

**Бо той самий callback type може викликатися з ISR, task, main loop або driver lock context.**

Від цього залежить, чи можна блокуватися, викликати malloc/printf, брати mutex, стартувати DMA або викликати інші driver APIs. Без документації caller легко напише callback, який працює в тесті, але deadlock-иться у реальній системі.

Правило: у callback contract завжди описуй context, allowed operations, reentrancy, lifetime і ownership.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
