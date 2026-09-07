---
id: emb-cppfound-0088
title: "Що виведе?"
description: "Why relational comparison of pointers to different objects is undefined in C."
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
int a=1,b=2;
int *p=&a,*q=&b;
printf("%d", p<q);
```

## Short answer

<span class="warn">Undefined behavior за стандартом C</span>. Реляційне порівняння (`<`, `>`) вказівників з різних об'єктів не визначено стандартом.

На практиці (більшість платформ, flat memory): результат залежить від розміщення змінних у пам'яті (порядок на стеку залежить від компілятора), тож не portable.

Дозволено: `p == q`, `p != q` – порівняння на рівність між будь-якими вказівниками. Реляційні – тільки в межах одного масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
