---
id: emb-cppfound-0083
title: "Яка адреса `arr`, `&arr`, `arr+1`, `&arr+1` якщо `int arr[4]` за адресою `0x1000`?"
description: "How array and pointer types produce different address increments."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

`arr` -> `0x1000` (decay до `int*`, вказує на arr[0]). `&arr` -> `0x1000` (вказує на весь масив, тип `int(*)[4]`). Та сама адреса, різний тип!

`arr+1` -> `0x1004` (крок = `sizeof(int) = 4`). `&arr+1` -> `0x1010` (крок = `sizeof(int[4]) = 16`).

Ось де різниця типів проявляється: однакова початкова адреса, різний крок.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
