---
id: emb-dtypes-0069
title: "Що таке linker script і яку роль він відіграє у розміщенні секцій?"
description: "Linker script визначає регіони пам'яті і правила, за якими кожна секція потрапляє у Flash чи RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

**Linker script** (`.ld` файл) - конфігурація linker-а, що визначає:

`MEMORY` блок: іменовані регіони пам'яті:
`FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K`
`RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K`.

`SECTIONS` блок: куди розмістити кожну секцію:
`.text : { *(.text*) } > FLASH`
`.data : { *(.data*) } > RAM AT> FLASH`

Linker генерує символи `_sdata`, `_edata`, `_sidata` для startup code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
