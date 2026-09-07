---
id: emb-fnptr-0023
title: "Що таке interrupt vector table з точки зору function pointers?"
description: "Це таблиця адрес handler-функцій, яку CPU використовує при exception/interrupt entry."
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

**Це таблиця адрес handler-функцій**, яку CPU використовує при exception/interrupt entry.

На Cortex-M vector table починається зі stack pointer value, а далі містить адреси Reset_Handler, NMI_Handler, HardFault_Handler та IRQ handlers. Це не звичайний C callback API, але концептуально це table of function entry addresses.

Правило: ISR handler signature і placement vector table мають відповідати startup code, linker script і ABI платформи.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
