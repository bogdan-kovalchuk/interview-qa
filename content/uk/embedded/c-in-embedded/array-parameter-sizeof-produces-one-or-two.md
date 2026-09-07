---
id: emb-cppfound-0016
title: "Trap: `void f(int arr[]) { int n = sizeof(arr)/sizeof(arr[0]); }` – яке значення `n`?"
description: "Why the array-length idiom fails for an array parameter."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

`n = 1` (на 32-bit) або `n = 2` (на 64-bit).

У параметрі функції `int arr[]` ≡ `int *arr` – decay до вказівника. `sizeof(arr) = sizeof(int*) = 4` (або 8). `sizeof(arr[0]) = sizeof(int) = 4`. Тому `4/4 = 1`;

<span class="warn">Не 8, не 256, не розмір масиву</span> – лише 1 або 2;

Завжди передавай розмір явно: `void f(int *arr, size_t n)`; Захист: `_Static_assert` у caller.[^embeddedinterviewlab]

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
