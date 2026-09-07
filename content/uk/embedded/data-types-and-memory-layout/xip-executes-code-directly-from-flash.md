---
id: emb-dtypes-0064
title: "Що таке XIP (Execute in Place) у embedded?"
description: "XIP означає, що CPU виконує код прямо з Flash без попереднього копіювання у RAM."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**XIP** (Execute in Place) - режим де CPU виконує код безпосередньо з Flash без копіювання у RAM.

NOR Flash підтримує random byte access -> CPU може адресувати та виконувати інструкції прямо. Більшість Cortex-M MCU використовують XIP за замовчуванням.

**Переваги**: не витрачається RAM на код, менший boot time. <span class="warn">Недолік</span>: Flash повільніша (wait states); Для часокритичних ISR: `__attribute__((section(".ramcode")))`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
