---
id: emb-cppfound-0093
title: "Що виведе?"
description: "Why array subscripting and pointer arithmetic are equivalent in C."
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
int arr[4]={10,20,30,40};
printf("%d %d",*(arr+3), arr[3]);
```

## Short answer

Обидва виводять `40`.

`*(arr+3)` -> pointer arithmetic: зсув на 3 елементи, розіменування = `arr[3] = 40`. `arr[3]` -> subscript operator, за визначенням = `*(arr+3)`.

Вони **ідентичні за стандартом**. Компілятор генерує однаковий машинний код для обох варіантів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
