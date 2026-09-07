---
id: emb-cppfound-0081
title: "Trap: чи коректно у C99?"
description: "Whether a pointer to a C99 compound literal remains valid within its block."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
int *p = &(int){5};
printf("%d", *p);
```

## Short answer

**Так, коректно** у межах того ж блоку. `(int){5}` – compound literal (C99): тимчасовий об'єкт зі storage duration автоматичного блоку.

<span class="warn">Але dangling pointer</span> якщо вийти за межі блоку: `int *p; { p = &(int){5}; } *p; // UB – блок закінчився`

GCC може не попередити. Безпечне використання: лише у тому ж scope де literal визначений.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
