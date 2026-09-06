---
id: emb-patterns-0016
title: "Як прочитати багатобітове поле (mask-and-shift)?"
description: "Накладаємо маску поля, потім зсуваємо вниз до позиції 0."
track: embedded
section: common-code-patterns
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
#define PRESC_MASK  (0x7U << 4) // bits [6:4]
#define PRESC_SHIFT 4
uint8_t p = (reg & PRESC_MASK) >> PRESC_SHIFT;
```

**Накладаємо маску поля, потім зсуваємо вниз до позиції 0.**

`reg & PRESC_MASK` лишає лише біти [6:4], `>> PRESC_SHIFT` приводить їх до значення 0..7.

Правило: для кожного поля визначай пару MASK+SHIFT і використовуй їх послідовно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
