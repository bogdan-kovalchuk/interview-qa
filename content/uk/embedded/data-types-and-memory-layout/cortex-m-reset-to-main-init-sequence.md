---
id: emb-dtypes-0007
title: "Яка послідовність ініціалізації C runtime до виклику `main()` на Cortex-M?"
description: "Апаратура читає vector table, копіює .data, обнуляє .bss і лише тоді викликає main()."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  en: 3
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

Апаратура читає Vector Table: SP отримує значення за адресою `0x00000000`, а PC – адресу Reset Handler з `0x00000004`. Startup code копіює `.data` з Flash (LMA) у RAM (VMA), обнуляє `.bss`, викликає глобальні C++ конструктори (якщо є) і нарешті `main()`.

Локальні змінні в `main()` - на стеку, <span class="warn">не ініціалізуються</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
