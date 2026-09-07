---
id: emb-dtypes-0036
title: "Trap: `sizeof(arr)/sizeof(arr[0])` - де цей трюк НЕ працює?"
description: "Переданий у функцію масив розпадається на вказівник, тож sizeof(arr) там дає розмір вказівника, а не масиву."
track: embedded
section: data-types-and-memory-layout
level: middle
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

При передачі масиву у функцію: `void f(int arr[]) { int n = sizeof(arr)/sizeof(arr[0]); }`

Тут `arr` - не масив, а <span class="warn">pointer</span> на перший елемент (`int*`). `sizeof(arr) = sizeof(int*) = 4 або 8`. Результат - неправильний.

Правильно: передавати розмір явно або використовувати `sizeof` тільки для масивів у тому ж scope де вони оголошені. У C++: `std::array` або `std::span`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
