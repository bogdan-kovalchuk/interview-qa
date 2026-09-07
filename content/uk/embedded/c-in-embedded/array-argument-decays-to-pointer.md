---
id: emb-cppfound-0082
title: "Що таке pointer decay при передачі масиву як аргументу функції?"
description: "Why an array argument becomes a pointer to its first element."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

При передачі масиву у функцію він **автоматично перетворюється** на вказівник на перший елемент (decay).

`int arr[8];` `f(arr)` -> `f(int *)` – функція отримує вказівник.

Наслідки:
- `sizeof(arr)` всередині функції = `sizeof(int*)`, не 32;
- Нема copy – функція отримує доступ до оригінального масиву;
- Нема range checking.

Рішення: `f(int arr[], size_t n)` або у C++: `template<size_t N> f(int (&arr)[N])`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
