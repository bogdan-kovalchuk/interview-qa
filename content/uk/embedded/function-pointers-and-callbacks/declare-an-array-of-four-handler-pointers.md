---
id: emb-fnptr-0047
title: "Як оголосити масив із 4 handler-ів `void handler(void)`?"
description: "Масив оголошують як void (*handlers[4])(void), а читабельніше – через typedef handler_t handlers[4]."
track: embedded
section: function-pointers-and-callbacks
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

## Short answer

Так. Безпосереднє оголошення масиву, або читабельніше – через typedef:

```c
void (*handlers[4])(void);

typedef void (*handler_t)(void);
handler_t handlers[4];
```

Правило: у складних деклараціях function pointer array майже завжди варто використовувати typedef.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
