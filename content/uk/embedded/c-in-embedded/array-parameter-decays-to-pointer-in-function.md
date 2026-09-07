---
id: emb-cppfound-0006
title: "Trap: чому `sizeof(arr)` у функції повертає 4 або 8, а не розмір масиву?"
description: "Why an array parameter is treated as a pointer inside a function."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

При передачі масиву у функцію він <span class="warn">decay-ується до вказівника</span>: `void f(int arr[])` ≡ `void f(int *arr)`.

`sizeof(arr)` всередині функції = `sizeof(int*)` = 4 або 8 (розмір вказівника), а не розмір масиву.

Реальний кейс: змінили `int16_t buffer[256]` на `int16_t *buffer`, але залишили `sizeof(buffer)/sizeof(buffer[0])` -> обробляли лише 2 елементи замість 256.

Рішення: передавай розмір явно: `void f(int *arr, size_t n)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
