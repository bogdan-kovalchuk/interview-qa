---
id: emb-cppfound-0032
title: "Що виведе?"
description: "How pointer subtraction reports the number of elements between pointers."
track: embedded
section: c-in-embedded
level: junior
type: concept
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
int arr[]={1,2,3,4,5};
int *p=arr+4;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`3`.

Відняття вказівників (`p - q`) повертає тип `ptrdiff_t` – кількість **елементів між ними**, не байт: `(arr+4) - (arr+1) = 3` елементи.

`%td` – формат для `ptrdiff_t`. Результат може бути від'ємним якщо `q > p`.

Фізично: байтова різниця = `3 * sizeof(int) = 12` байт, але pointer subtraction ділить на `sizeof(int)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
