---
id: emb-macros-0010
title: "Навіщо statement-макрос обгортають у `do { ... } while(0)`?"
description: "Щоб макрос із кількох інструкцій поводився як один statement і коректно працював з if/else та крапкою з комою."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
#define LOG_ERR(m) do { \
    uart_puts("[ERR] "); \
    uart_puts(m); \
} while (0)
```

## Short answer

**Щоб макрос із кількох інструкцій поводився як один statement** і коректно працював з `if/else` та крапкою з комою.

`do { ... } while(0)` утворює єдиний блок, який вимагає `;` у кінці виклику, тому `if (c) LOG_ERR(x); else ...` компілюється правильно.

Правило: будь-який multi-statement макрос обгортай у `do { ... } while(0)`; з `\` у кінці кожного рядка для продовження.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
