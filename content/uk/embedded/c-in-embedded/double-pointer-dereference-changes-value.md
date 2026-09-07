---
id: emb-cppfound-0045
title: "Що виведе?"
description: "How double dereferencing changes an object through a pointer chain."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 4
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
int x=10;
int *p=&x;
int **pp=&p;
**pp=20;
printf("%d",x);
```

## Short answer

`20`.

Ланцюжок: `pp` -> `&p` (адреса вказівника `p`), `*pp` -> розіменування = сам вказівник `p` (адреса `x`), `**pp` -> подвійне розіменування = значення `x`.

`**pp = 20` -> запис 20 у `x` через ланцюжок, тож `x` стає 20. Всі три: `x`, `*p`, `**pp` тепер = 20.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
