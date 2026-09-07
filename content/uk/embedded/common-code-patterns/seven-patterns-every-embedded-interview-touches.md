---
id: emb-patterns-0001
title: "Які сім базових патернів embedded C варто знати на інтерв'ю?"
description: "State machines, ring buffers, bit manipulation, error handling, memory-mapped I/O, volatile-safe patterns, guard clauses."
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

**State machines, ring buffers, bit manipulation, error handling, memory-mapped I/O, volatile-safe patterns, guard clauses.**

Хороша embedded-версія цих патернів зазвичай heap-free і має чітку відповідь, чи безпечна вона для ISR (interrupt service routine) / main loop взаємодії. Не кожен патерн автоматично ISR-safe – безпека залежить від shared state, atomicity і blocking calls.

Правило: на питання «які патерни ти використовуєш» називай їх із trade-off'ами, а не просто перелік.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
