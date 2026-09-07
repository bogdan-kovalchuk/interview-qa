---
id: emb-cppfound-0060
title: "Що виведе?"
description: "How multidimensional-array pointer arithmetic reaches an element."
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
int arr[3][3]={{1,2,3},{4,5,6},{7,8,9}};
printf("%d", *(*(arr+1)+2));
```

## Short answer

`6`.

`arr+1` -> вказівник на другий рядок `arr[1]` (тип `int(*)[3]`). `*(arr+1)` -> decay до `int*`, вказує на `arr[1][0] = 4`. `*(arr+1)+2` -> вказує на `arr[1][2] = 6`. `*(*(arr+1)+2)` -> значення = `6`.

Еквівалентно: `arr[1][2]`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
