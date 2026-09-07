---
id: emb-patterns-0042
title: "Що має вміти кандидат у питаннях про embedded code patterns?"
description: "Писати FSM (finite state machine) у обох формах: switch і table; пояснювати trade-off-и; будувати ring buffer на степені двійки з race від count; робити bit operations через unsigned mask-and-shift."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

**Писати FSM (finite state machine) у обох формах: switch і table; пояснювати trade-off-и; будувати ring buffer на степені двійки з race від `count`; робити bit operations через unsigned mask-and-shift.**

Плюс: консистентні return codes із перевіркою всіх результатів, `volatile` для регістрів, guard clauses для null/діапазону.

Правило: до кожного патерну май відповідь «коли застосовувати», «чи ISR-safe (interrupt service routine safe)» і «чому без heap».[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
