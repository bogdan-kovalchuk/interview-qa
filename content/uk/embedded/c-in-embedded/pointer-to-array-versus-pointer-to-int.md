---
id: emb-cppfound-0015
title: "Що таке `int (*p)[8]` і чим відрізняється від `int *p`?"
description: "How a pointer to an array differs from a pointer to an int."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`int *p` – вказівник на `int`, тож `p+1` -> +4 байти (один `int`), а `int (*p)[8]` – **вказівник на масив** з 8 `int`, де `p+1` -> +32 байти (один масив із 8 елементів).

Використання: при роботі з 2D масивами: `int arr[3][8]; int (*p)[8] = arr;`. `p[1]` -> другий рядок; `p[1][3]` -> `arr[1][3]`.

Правило читання: `(*p)` -> "вказівник на" (дужки важливі через пріоритет операторів).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
