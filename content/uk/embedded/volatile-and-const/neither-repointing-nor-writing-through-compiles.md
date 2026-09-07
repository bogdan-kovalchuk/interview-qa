---
id: emb-volconst-0023
title: "Що скомпілюється, а що ні: `const int * const p`?"
description: "Не скомпілюються обидва записи: p = 3 і p = &y."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
int x = 1, y = 2;
const int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**Не скомпілюються обидва записи: `*p = 3` і `p = &y`.**

`const int * const p` означає const pointer to const int. Через цей pointer не можна змінити ні pointed-to value, ні сам pointer value.

Embedded-приклад: fixed pointer на read-only lookup table або на read-only register, якщо додати ще `volatile` для hardware.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
