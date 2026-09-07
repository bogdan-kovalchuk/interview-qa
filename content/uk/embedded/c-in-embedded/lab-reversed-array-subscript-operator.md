---
id: emb-cppfound-0078
title: "Що виведе?"
description: "Why the reversed subscript expression is valid C pointer arithmetic."
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
int arr[]={5,10,15};
printf("%d", 2[arr]);
```

## Short answer

`15`.

`2[arr]` -> за стандартом: `*(2 + arr)` – ідентично `arr[2]`. Subscript operator симетричний через комутативність додавання: `arr[2] == *(arr+2) == *(2+arr) == 2[arr]`.

Всі 4 форми дають однаковий код. `2[arr]` – валідний C, але нечитабельний. Зустрічається як питання на інтерв'ю для перевірки розуміння pointer arithmetic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
