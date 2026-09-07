---
id: emb-fnptr-0058
title: "Що має містити хороша відповідь на інтерв'ю про callbacks в embedded?"
description: "Механізм, контракт і ризики."
track: embedded
section: function-pointers-and-callbacks
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

**Механізм, контракт і ризики.**

Механізм: function pointer з конкретною сигнатурою. Контракт: хто реєструє, хто викликає, коли, з яким context pointer і lifetime. Ризики: null pointer, wrong signature UB, ISR context, dangling context, reentrancy, blocking calls, і валідація dispatch index.

Правило: сильна embedded-відповідь не зупиняється на синтаксисі `void (*cb)(void)`; вона пояснює runtime ownership і execution context.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
