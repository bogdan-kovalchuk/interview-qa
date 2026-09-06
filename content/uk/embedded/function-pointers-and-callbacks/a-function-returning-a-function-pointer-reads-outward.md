---
id: emb-fnptr-0048
title: "Як оголосити функцію, яка повертає function pointer?"
description: "Приклад без typedef: int (select_op(int id))(int, int); Це означає: select_op приймає int і повертає pointer на функцію, яка приймає два int і повертає int."
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

Приклад без typedef:

`int (*select_op(int id))(int, int);`

Це означає: `select_op` приймає `int` і повертає pointer на функцію, яка приймає два `int` і повертає `int`. Через typedef краще: `typedef int (*op_t)(int, int); op_t select_op(int id);`

Правило: якщо декларацію важко прочитати з першого разу, typedef – правильний інженерний вибір.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
