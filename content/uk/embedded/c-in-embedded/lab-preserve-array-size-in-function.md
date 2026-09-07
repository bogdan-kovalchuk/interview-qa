---
id: emb-cppfound-0062
title: "Як передати масив у функцію і зберегти інформацію про його розмір?"
description: "Ways to preserve array length when array-to-pointer decay removes it."
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

Оскільки масив decay-ується до вказівника, розмір <span class="warn">не передається автоматично</span>. Варіанти:

1) **Явний параметр**: `void f(int *arr, size_t n)` – найпростіше;
2) **Sentinel value**: null-terminator для рядків, спеціальне значення;
3) **Struct + масив**: `struct { int *data; size_t len; }`;
4) C++ **std::span** або `std::array<int,N>`.

Захист: `_Static_assert(sizeof(arr) != sizeof(int*), "Use real array")` у caller.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
