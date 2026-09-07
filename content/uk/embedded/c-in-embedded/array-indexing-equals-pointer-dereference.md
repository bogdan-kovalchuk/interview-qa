---
id: emb-cppfound-0013
title: "Розберіть?"
description: "Why array indexing and pointer dereferencing are equivalent."
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
int arr[3] = {1,2,3};
printf("%d %d", arr[2], *(arr+2));
```

## Short answer

Обидва вирази виводять **3** і є повністю еквівалентними за стандартом C.

`arr[2]` -> стандарт визначає як `*(arr+2)`: до адреси `arr` додається `2 * sizeof(int) = 8` байт, потім розіменовується.

Тому навіть `2[arr]` -> `*(2+arr)` -> 3 – теж коректно (через комутативність додавання, хоча й нечитабельно).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
