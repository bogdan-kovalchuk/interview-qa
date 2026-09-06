---
id: emb-fnptr-0013
title: "Чим function pointer відрізняється від callback?"
description: "Function pointer – це тип/значення, callback – архітектурний патерн."
track: embedded
section: function-pointers-and-callbacks
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

**Function pointer – це тип/значення, callback – архітектурний патерн.**

Function pointer може лежати в таблиці команд, vector table або vtable-like struct. Callback – це коли один модуль реєструє функцію, а інший модуль викликає її пізніше, зазвичай у відповідь на подію.

Embedded-приклад: `void (*isr)(void)` у vector table – function pointer; user hook `on_rx(ctx, byte)`, який викликає UART driver, – callback.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
