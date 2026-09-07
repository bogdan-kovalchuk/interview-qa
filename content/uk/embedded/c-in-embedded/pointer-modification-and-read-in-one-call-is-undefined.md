---
id: emb-cppfound-0050
title: "Що виведе?"
description: "Why modifying and reading a pointer in one printf call is undefined behavior."
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
int arr[5]={1,2,3,4,5};
int *p=arr;
printf("%d %d", *p++, *p);
```

## Short answer

<span class="warn">Undefined behavior</span> – порядок обчислення аргументів `printf` не визначений стандартом.

`p++` – post-increment: повертає поточне значення і збільшує. Але між обчисленням `*p++` і `*p` в межах одного виклику функції немає sequence point. Компілятор може обчислити аргументи у будь-якому порядку.

Результат залежить від компілятора/платформи. Краще: `printf("%d %d", arr[0], arr[1]);`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
