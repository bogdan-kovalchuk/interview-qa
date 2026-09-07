---
id: emb-dtypes-0075
title: "Що відбудеться? `int *p = (int*)malloc(10*sizeof(int)); p[10] = 0;`"
description: "malloc(10*sizeof(int)) виділяє лише p[0]..p[9], тож p[10] пише за межі виділеного блоку heap."
track: embedded
section: data-types-and-memory-layout
level: middle
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

<span class="warn">Out-of-bounds write на heap -> undefined behavior.</span>

`malloc(10*sizeof(int))` виділяє пам'ять для `p[0]..p[9]`. `p[10]` - за межами, перезаписує heap metadata або сусідній блок.

Наслідки:
1. Пошкодження heap metadata -> crash при наступному `malloc`/`free`;
2. Тихе пошкодження даних (проявляється пізніше).

Захист: `-fsanitize=address` при розробці, Valgrind на Linux, heap guard regions.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
