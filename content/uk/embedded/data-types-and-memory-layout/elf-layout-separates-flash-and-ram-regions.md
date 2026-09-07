---
id: emb-dtypes-0065
title: "Як виглядає типовий layout секцій у `.elf` файлі для Cortex-M?"
description: "Flash тримає .text, .rodata і LMA .data, а RAM тримає VMA .data, .bss, heap і stack."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

**Flash (ROM)**: `[.text][.rodata][.data LMA]`
**RAM**: `[.data VMA][.bss][heap ↑]...[stack ↓]`

LMA (Load Memory Address) - де байти зберігаються у Flash. VMA (Virtual Memory Address) - де CPU їх очікує у RAM. Startup code копіює LMA -> VMA для `.data`.

Перевірка: `arm-none-eabi-objdump -h firmware.elf` або `arm-none-eabi-size firmware.elf`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
