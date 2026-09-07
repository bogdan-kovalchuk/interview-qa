---
id: emb-fnptr-0001
title: "Що таке вказівник на функцію в C?"
description: "Вказівник на функцію зберігає адресу виконуваного коду функції з конкретною сигнатурою."
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

**Вказівник на функцію** зберігає адресу виконуваного коду функції з конкретною сигнатурою.

На відміну від object pointer, він не вказує на дані в RAM/Flash як звичайний об'єкт, а використовується для indirect call: код вирішує, яку функцію викликати, під час виконання. В embedded це основа callbacks, interrupt vector tables, driver HAL interfaces, state machines і command dispatch tables.

Правило: function pointer type має точно відповідати return type і parameter types функції, яку через нього викликають.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
