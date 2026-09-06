---
id: emb-fnptr-0010
title: "Що краще для optional callback: перевірка на `NULL` чи no-op function?"
description: "Обидва варіанти валідні, але no-op callback може спростити hot path."
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

Обидва варіанти валідні, але no-op callback може спростити hot path.

Якщо callback опційний і викликається часто, driver може ініціалізувати його функцією `static void noop(void *ctx) { (void)ctx; }`. Тоді код виклику не має гілки `if (cb)`. Але це має бути документовано, щоб callback pointer ніколи не залишався uninitialized.

Правило: для простого API перевірка на `NULL` зрозуміліша; для performance-critical dispatch table no-op entry може бути кращим.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
