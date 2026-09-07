---
id: emb-fnptr-0044
title: "Що таке state machine на function pointers?"
description: "Це таблиця state handlers або transition handlers, де поточний state вибирає функцію для обробки event-а."
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

**Це таблиця state handlers або transition handlers**, де поточний state вибирає функцію для обробки event-а.

Наприклад: `state = handlers[state](ctx, event);`. Це робить кожен state окремою функцією і зменшує великий nested `switch`. Для embedded protocol stacks це часто читабельно і тестовано по state handler-ах.

Правило: state enum має бути bounds-checked перед індексом у handler table.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
