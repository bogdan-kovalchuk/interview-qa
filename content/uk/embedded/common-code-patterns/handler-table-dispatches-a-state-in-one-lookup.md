---
id: emb-patterns-0004
title: "Як виглядає state machine на function-pointer table?"
description: "Масив вказівників на handler-и, індексований станом; диспетчеризація – один lookup, O(1)."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
typedef void (*handler_t)(oven_event_t e);
static const handler_t handlers[] = {
  [STATE_IDLE]    = on_idle,
  [STATE_HEATING] = on_heating,
  [STATE_ERROR]   = on_error,
};
handlers[*state](evt);
```

## Short answer

**Масив вказівників на handler-и, індексований станом; диспетчеризація – один lookup, O(1).**

Переваги: новий стан = нова функція + рядок таблиці, без змін наявного коду. Таблиця `static const` лежить у Flash (`.rodata`).

Правило: масштабовано для багатьох станів, але важче читати в дебагері.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
