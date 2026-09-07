---
id: emb-cppfound-0043
title: "Яке значення повертає `&arr` і як відрізняється від `arr` якщо `int arr[8]`?"
description: "Why <code>arr</code> and <code>&amp;arr</code> share an address but have different pointer types."
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

Обидва вирази дають **однакову числову адресу** (адресу першого елемента масиву), але мають різні **типи**:

`arr` -> decay до `int*`. `arr+1` -> +4 байти (один int). `&arr` -> `int(*)[8]` (вказівник на масив). `&arr+1` -> +32 байти (один масив).

Практично: `&arr` використовується для передачі у функцію що очікує `int(*)[8]` – зберігає розмір масиву у типі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
