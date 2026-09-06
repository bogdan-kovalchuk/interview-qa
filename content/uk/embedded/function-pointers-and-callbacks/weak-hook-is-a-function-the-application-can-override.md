---
id: emb-fnptr-0052
title: "Що таке weak callback hook у embedded firmware?"
description: "Weak hook – це weak function, яку application може перевизначити сильною реалізацією."
track: embedded
section: function-pointers-and-callbacks
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

**Weak hook** – це weak function, яку application може перевизначити сильною реалізацією.

Startup files часто мають `void SysTick_Handler(void) __attribute__((weak));` або weak default handlers. Якщо user code визначить функцію з таким самим ім'ям, linker вибере user implementation.

Правило: weak hooks прості для startup/board support, але для runtime-multiple instances краще explicit callback registration.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
