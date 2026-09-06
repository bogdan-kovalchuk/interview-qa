---
id: emb-volconst-0058
title: "Що означає `volatile uint8_t rx_buf[64]` для DMA receive buffer?"
description: "Кожен елемент масиву має volatile-qualified type, тому читання rx_buf[i] має бути реальним memory access."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

**Кожен елемент масиву має volatile-qualified type**, тому читання `rx_buf[i]` має бути реальним memory access.

Це може бути потрібно, якщо DMA змінює bytes поза control flow CPU. Але це не вирішує cache coherency, не гарантує, що DMA вже завершив запис, і не робить multi-byte parsing атомарним.

Правило: volatile buffer може бути частиною DMA protocol, але потрібні completion flags, barriers/cache maintenance і ownership discipline.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
