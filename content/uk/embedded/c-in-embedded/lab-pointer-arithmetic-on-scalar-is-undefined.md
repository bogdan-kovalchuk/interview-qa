---
id: emb-cppfound-0066
title: "Trap: що виведе?"
description: "Why pointer arithmetic on a pointer to a standalone object is undefined."
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

## Question code

```c
int a=1;
int *p=&a;
int *q=&a;
q++;
printf("%d",*q);
```

## Short answer

<span class="warn">Undefined behavior</span>. `q++` -> `q` тепер вказує на адресу одразу після `a` на стеку. Це не елемент масиву – лише окрема змінна.

Pointer arithmetic визначена тільки в межах масиву (або struct за умовами). Для двох окремих змінних – навіть якщо вони поруч на стеку – `&a + 1` -> UB;

Компілятор може розмістити `a` у регістрі без адреси у пам'яті -> `*q` читає сміття.[^embeddedinterviewlab]

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
