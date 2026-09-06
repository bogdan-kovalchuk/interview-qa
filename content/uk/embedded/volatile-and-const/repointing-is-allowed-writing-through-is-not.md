---
id: emb-volconst-0021
title: "Що скомпілюється, а що ні: `const int *p`?"
description: "p = &y скомпілюється, p = 3 не скомпілюється."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
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

## Short answer

```c
int x = 1, y = 2;
const int *p = &x;
p = &y;
*p = 3;
```

**`p = &y` скомпілюється, `*p = 3` не скомпілюється.**

`const int *p` означає pointer to const int. Const стосується даних, на які вказує `p`, а не самого pointer. Тому pointer можна змінити, але запис через нього заборонений.

Правило: якщо `const` ліворуч від `*`, захищені pointed-to data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
