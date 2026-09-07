---
id: emb-cppfound-0020
title: "Що виведе?"
description: "How dereferencing an element of an array of pointers accesses its value."
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
int a=1,b=2,c=3;
int *arr[3]={&a,&b,&c};
printf("%d",*arr[1]);
```

## Short answer

`2`.

`int *arr[3]` – масив з 3 вказівників на `int`. `arr[1]` -> другий елемент = `&b`. `*arr[1]` -> розіменування `&b` -> значення `b = 2`.

Зберігання: `arr` – масив адрес (3 × 4 байти = 12 байт). Кожен елемент – окрема адреса; Зміна `*arr[1] = 99` -> змінить `b`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
