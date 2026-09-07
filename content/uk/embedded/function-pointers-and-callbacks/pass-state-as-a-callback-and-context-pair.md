---
id: emb-fnptr-0030
title: "Як правильно передати стан у C callback без global variables?"
description: "Через пару callback + context pointer."
track: embedded
section: function-pointers-and-callbacks
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

## Short answer

Через пару `callback + context pointer`.

Приклад: `timer_start(timer, on_timeout, &app);` – driver зберігає `on_timeout` і `&app`. Коли timer спрацьовує, він викликає `on_timeout(&app)`. Callback приводить `void *` назад до `struct App *`.

Правило: callback не повинен здогадуватись про global instance; context робить залежність явною.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
