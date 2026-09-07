---
id: emb-volconst-0039
title: "Trap: чи достатньо `volatile` для DMA buffer?"
description: "Не завжди. volatile може змусити CPU перечитувати descriptor або flag, які змінює DMA."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

## Short answer

<span class="warn">Не завжди.</span>

`volatile` може змусити CPU перечитувати descriptor або flag, які змінює DMA. Але воно не вирішує cache coherency, alignment, ownership, memory barriers і race conditions. На Cortex-M7 з D-cache DMA може записати RAM, а CPU все ще читатиме старі cache lines.

Захист: крім правильних volatile flags/descriptors, використовуй non-cacheable memory або cache clean/invalidate, barriers і чіткий ownership protocol між CPU та DMA.[^embeddedinterviewlab]

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
