---
id: emb-dtypes-0015
title: "Що виведе `sizeof(\"hello\")` та `strlen(\"hello\")`?"
description: "sizeof рахує null-термінатор і дає 6, а strlen рахує символи без нього і дає 5."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`sizeof("hello")` -> **6**: рядковий літерал - масив `{'h','e','l','l','o','\0'}` (6 байтів), а `sizeof` compile-time рахує null-terminator. `strlen("hello")` -> **5**: runtime функція рахує символи до (не включаючи) `'\0'`.

Типова помилка: виділити `malloc(strlen(s))` без +1 для `'\0'` -> buffer overflow.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
