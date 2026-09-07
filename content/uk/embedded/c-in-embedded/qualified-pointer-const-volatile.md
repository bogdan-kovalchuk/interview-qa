---
id: emb-cppfound-0092
title: "Що таке qualified pointer (`volatile`, `const`) і як qualifier поширюється?"
description: "How const and volatile qualifiers affect pointed-to data and pointer use."
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

Qualifier – частина типу вказівника, що вказує на властивості даних або самого вказівника.

`const int *p` – qualifier на дані: не можна змінити `*p`. Можна дати менш qualified вказівник: `int *p` -> `const int *q = p` (додавання const – OK), зворотне -> warning/error.

`volatile uint32_t *reg` – кожен доступ реально виконується (для registers).

Правило: можна **додавати** qualifier при присвоєнні, але <span class="warn">не знімати</span> без explicit cast.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
