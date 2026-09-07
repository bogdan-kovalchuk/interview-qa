---
id: emb-cppfound-0008
title: "Що виведе?"
description: "How pointer arithmetic accesses the third array element."
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
int arr[5] = {10,20,30,40,50};
int *p = arr;
printf("%d", *(p+2));
```

## Short answer

`30`.

`arr` decay-ується до вказівника на перший елемент. `p = arr` -> `p` вказує на `arr[0]`.

`p+2` -> вказівник на `arr[2]` (кроком `2 * sizeof(int) = 8` байт на 32-bit). `*(p+2)` -> розіменування -> `arr[2] = 30`.

За стандартом: `arr[i] ≡ *(arr+i) ≡ *(i+arr) ≡ i[arr]` – всі чотири форми еквівалентні.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
