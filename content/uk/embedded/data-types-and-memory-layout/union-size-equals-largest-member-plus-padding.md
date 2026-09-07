---
id: emb-dtypes-0052
title: "Скільки пам'яті займає union і як розраховується його розмір?"
description: "Розмір union дорівнює розміру найбільшого поля плюс padding для вирівнювання."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

`sizeof(union)` = **розмір найбільшого поля** + trailing padding для задоволення alignment.

Всі поля union займають одну і ту ж область пам'яті.

Приклад: `union { char c; int x; double d; }` -> sizeof = 8 (double найбільший, align = 8).

Корисний для: type punning, variant types, byte-level inspection. У C++ активним може бути лише одне поле.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
