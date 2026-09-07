---
id: emb-volconst-0038
title: "Чому `volatile` не є memory barrier?"
description: "volatile обмежує оптимізації доступів до volatile-об'єктів, але не є повноцінним CPU/compiler memory barrier для всієї пам'яті."
track: embedded
section: volatile-and-const
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

**`volatile` обмежує оптимізації доступів до volatile-об'єктів, але не є повноцінним CPU/compiler memory barrier для всієї пам'яті.**

Компілятор має зберігати порядок volatile accesses відносно інших volatile accesses, але це не означає синхронізацію cache, bus ordering, DMA visibility або inter-core ordering. На Cortex-M для device memory порядок часто сильніший, але для DMA та периферійних сценаріїв можуть бути потрібні barriers і cache maintenance.

Правило: для hardware ordering використовуй архітектурні primitives на кшталт `__DMB()`, `__DSB()`, `__ISB()`, коли цього вимагає reference manual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
