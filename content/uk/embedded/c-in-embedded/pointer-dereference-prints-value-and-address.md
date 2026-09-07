---
id: emb-cppfound-0002
title: "Що виведе?"
description: "How dereferencing and pointer values differ in a C example."
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
int x = 42;
int *p = &x;
printf("%d %p", *p, (void*)p);
```

## Short answer

`*p` -> `42` (розіменування – читає значення `x`). `p` -> адреса змінної `x` (наприклад, `0x2000FFE0` на стеку Cortex-M).

Важливо: `p` і `x` – різні об'єкти. `p` зберігає адресу, `x` – значення. Зміна `*p = 100` змінює `x`. Зміна `p = &y` не змінює `x`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
