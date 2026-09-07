---
id: emb-cppfound-0028
title: "Що таке `restrict` і навіщо він потрібен у embedded?"
description: "How restrict communicates non-aliasing to the compiler."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
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

`restrict` (C99) – кваліфікатор вказівника, що гарантує компілятору: через цей вказівник і через жоден інший вказівник у цій функції **не відбувається aliasing** (перекриття областей пам'яті).

Приклад: `void add(int * restrict dst, const int * restrict src, int n)`.

Дає компілятору дозвіл на агресивну оптимізацію (векторизація, підкачка у регістри). Важливо для DSP, crypto, memcpy-like функцій. Якщо aliasing все ж є – UB.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
