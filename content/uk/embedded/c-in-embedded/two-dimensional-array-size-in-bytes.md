---
id: emb-cppfound-0024
title: "Що виведе?"
description: "How sizeof reports the size of a two-dimensional array."
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
int arr[3][4];
printf("%zu", sizeof(arr));
```

## Short answer

**48** байт.

`arr` – 2D масив: 3 рядки × 4 стовпці × `sizeof(int) = 4` байти = 48B.

`sizeof(arr[0])` = `sizeof(int[4])` = 16B (один рядок). `sizeof(arr[0][0])` = `sizeof(int)` = 4B.

Кількість рядків: `sizeof(arr)/sizeof(arr[0]) = 48/16 = 3`. Цей трюк працює лише у тому ж scope де оголошений масив.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
