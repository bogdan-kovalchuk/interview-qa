---
id: emb-cppfound-0055
title: "Як реалізувати swap двох int через вказівники?"
description: "How to swap two integers through pointer parameters."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 5
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

## Short answer

```c
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

Виклик: `int x=5, y=10; swap(&x, &y);` -> `x=10, y=5`.

Без tmp через XOR: `*a^=*b; *b^=*a; *a^=*b;` – але <span class="warn">якщо `a == b`, значення обнулиться</span> (обидва вказівники на один об’єкт, а `x ^ x == 0`). Передавай завжди адреси (через `&` у caller), не значення.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
