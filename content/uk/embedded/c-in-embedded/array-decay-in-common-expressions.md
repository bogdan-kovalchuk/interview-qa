---
id: emb-cppfound-0009
title: "Що таке array decay і в яких контекстах масив перетворюється на вказівник?"
description: "When an array is converted to a pointer to its first element."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

**Array decay** – автоматичне перетворення масиву на вказівник на його перший елемент.

Відбувається у більшості виразів:
- При передачі у функцію: `f(arr)` -> функція отримує `int*`;
- У арифметиці: `arr+1` -> `int*`;
- При присвоєнні: `int *p = arr`.

Наслідок: функція <span class="warn">втрачає інформацію про розмір</span> масиву. Тип стає `int*`, а не `int[N]`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
