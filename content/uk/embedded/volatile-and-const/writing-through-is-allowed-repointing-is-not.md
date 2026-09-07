---
id: emb-volconst-0022
title: "Що скомпілюється, а що ні: `int * const p`?"
description: "p = 3 скомпілюється, p = &y не скомпілюється."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**`*p = 3` скомпілюється, `p = &y` не скомпілюється.**

`int * const p` означає const pointer to int. Адреса, збережена в `p`, незмінна, але сам об'єкт `x` mutable.

Правило: якщо `const` праворуч від `*`, захищений pointer; якщо ліворуч від `*`, захищені дані.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
