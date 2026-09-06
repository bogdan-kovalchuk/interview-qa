---
id: emb-fnptr-0024
title: "Як оголосити тип ISR handler без аргументів і без return value?"
description: "Типово: typedef void (isr_handler_t)(void); Після цього vector table може містити isr_handler_t entries."
track: embedded
section: function-pointers-and-callbacks
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

Типово:

`typedef void (*isr_handler_t)(void);`

Після цього vector table може містити `isr_handler_t` entries. На Cortex-M реальний vector table часто має спеціальний layout, бо перший entry – initial stack pointer, не function pointer.

Правило: не змішуй data pointer і function pointer без розуміння startup ABI; vector table часто описують окремими linker/startup constructs.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
