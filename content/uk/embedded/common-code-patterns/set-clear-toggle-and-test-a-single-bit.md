---
id: emb-patterns-0014
title: "Як виглядають чотири базові бітові операції?"
description: "Set – OR з маскою, clear – AND з інверсією маски, toggle – XOR, test – AND; маску роблять через BIT32(n)."
track: embedded
section: common-code-patterns
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

## Short answer

**Set / Clear / Toggle / Test:**

```c
#define BIT32(n) (UINT32_C(1) << (n))

reg |=  BIT32(n);   // set
reg &= ~BIT32(n);   // clear
reg ^=  BIT32(n);   // toggle
if (reg & BIT32(n)) { ... } // test
```

Set – OR, clear – AND з інверсією маски, toggle – XOR, test – AND.

Правило: ці чотири ідіоми – основа конфігурації регістрів і прапорців; для 32-bit регістрів використовуй 32-bit unsigned literal.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
