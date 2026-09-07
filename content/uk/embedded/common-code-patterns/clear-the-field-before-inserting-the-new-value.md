---
id: emb-patterns-0017
title: "Як записати багатобітове поле, не зачепивши інші біти (read-modify-write)?"
description: "Спершу очисти біти поля (& ~MASK), потім вклади нове значення (зсунуте і замасковане)."
track: embedded
section: common-code-patterns
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
reg = (reg & ~PRESC_MASK)
    | ((value << PRESC_SHIFT) & PRESC_MASK);
```

## Short answer

**Спершу очисти біти поля (`& ~MASK`), потім вклади нове значення (зсунуте і замасковане).**

Маскування `value` по `& MASK` захищає від переповнення в сусідні біти, якщо `value` завеликий.

Правило: запис поля регістра – це завжди clear + set, інакше затреш сусідні налаштування.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
