---
id: emb-cppfound-0063
title: "Що виведе?"
description: "How a function changes the caller's array through a pointer parameter."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
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
void f(int *p, int n){
  p[0]=99;
} int a[3]={1,2,3};
f(a,3);
printf("%d",a[0]);
```

## Short answer

`99`.

`a` decay-ується до вказівника. Функція `f` отримує `int*` – вказівник на перший елемент `a[0]`. `p[0] = 99` -> змінює `a[0]` у caller.

Масиви у C передаються by reference (через вказівник на перший елемент) – функція може змінювати оригінальні дані. Якщо потрібна тільки читання: `const int *p`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
