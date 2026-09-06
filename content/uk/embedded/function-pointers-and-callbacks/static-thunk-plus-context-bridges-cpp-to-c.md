---
id: emb-fnptr-0041
title: "Як зробити C callback для C++ object-а?"
description: "Використовують static thunk + context pointer."
track: embedded
section: function-pointers-and-callbacks
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

Використовують static thunk + context pointer.

`static void thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` `uart_register(thunk, this);`

Static member function не має прихованого `this` і сумісна зі звичайним function pointer, якщо signature збігається. `ctx` повертає object instance вручну.

Правило: це стандартний bridge між C HAL і C++ class design.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
