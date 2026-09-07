---
id: emb-cppfound-0010
title: "Що поверне `sizeof(arr)` vs `sizeof(p)` якщо `int arr[8]; int *p = arr;`?"
description: "Why sizeof an array differs from sizeof a pointer."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

`sizeof(arr)` -> **32** (8 елементів × 4 байти = 32B). `sizeof` на справжньому масиві повертає загальний розмір у байтах.

`sizeof(p)` -> **4** (або 8 на 64-bit). Вказівник зберігає лише адресу – його розмір = розрядність архітектури.

Ключова відмінність: масив і вказівник мають однаковий тип елементів, але `sizeof` дає зовсім різні результати.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
