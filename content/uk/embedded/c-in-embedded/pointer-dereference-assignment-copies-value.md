---
id: emb-cppfound-0027
title: "Що виведе?"
description: "Why dereferencing pointers copies the pointed-to value."
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

## Question code

```c
int a=5, b=10;
int *p=&a, *q=&b;
*p=*q;
printf("%d %d",a,b);
```

## Short answer

`a=10, b=10`.

`*p = *q` – копіює **значення** `*q` (тобто `b=10`) у `*p` (тобто у `a`). Самі вказівники `p` і `q` не змінюються.

Якби `p = q` (без *) – обидва вказівники вказували б на `b`, а `a` лишився б `5`.

Типова помилка: плутати присвоєння вказівників та значень.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
