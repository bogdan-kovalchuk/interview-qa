---
id: emb-cppfound-0029
title: "Як правильно передати 2D масив у функцію та звернутись до елемента `[2][3]`?"
description: "Why a two-dimensional array parameter needs its inner dimension."
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

Для статично розмірного масиву потрібно вказати **розмір внутрішнього виміру**: `void f(int arr[][4], int rows) { arr[2][3] = 99; }` або еквівалентно: `void f(int (*arr)[4], int rows) { ... }`

Без розміру компілятор не знає крок рядка (stride). `arr[i][j]` -> `*(*(arr+i)+j)` -> в пам'яті: `arr + i*4*sizeof(int) + j*sizeof(int)`.

Для динамічного: передавай як `int *` і обчислюй offset вручну.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
