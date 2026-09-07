---
id: emb-cppfound-0065
title: "Яка різниця між `int *arr[5]` і `int (*arr)[5]` у пам'яті?"
description: "How an array of pointers differs from a pointer to an array."
track: embedded
section: c-in-embedded
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

`int *arr[5]` – масив із 5 вказівників. Розмір: `5 × sizeof(int*) = 20 байт`. Кожен з 5 елементів – адреса якогось int, можуть вказувати у різні місця пам'яті.

`int (*arr)[5]` – один вказівник на масив із 5 int. Розмір `arr` = `sizeof(int*) = 4` байти; `arr+1` -> зміщення на `5 × sizeof(int) = 20` байт.

Читай: дужки навколо `*arr` – "вказівник на".[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
