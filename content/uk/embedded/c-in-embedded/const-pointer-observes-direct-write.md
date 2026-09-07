---
id: emb-cppfound-0095
title: "Що виведе?"
description: "Why a pointer to const cannot write while still observing direct changes to a non-const object."
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
int x=5;
const int *p=&x;
x=10;
printf("%d",*p);
```

## Short answer

`10`.

`const int *p = &x` – вказівник на const int: забороняє змінювати `*p` (через цей вказівник). Але `x` – не const, тож зміна `x = 10` через пряме ім'я – легальна.

`*p` читає значення `x` = 10. `const` захищає від запису через `p`, але не робить `x` незмінним – це важлива відмінність: `const int *p` vs `const int x`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
