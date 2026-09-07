---
id: emb-fnptr-0002
title: "Як прочитати декларацію `void (*handler)(int)`?"
description: "handler є вказівником на функцію, яка приймає int і повертає void."
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

**`handler` є вказівником на функцію, яка приймає `int` і повертає `void`.**

Дужки навколо `*handler` критичні: вони кажуть, що pointer належить імені `handler`, а не return type. Без дужок це була б інша декларація.

Правило читання: починай з імені. `handler` is pointer to function taking `int` returning `void`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
