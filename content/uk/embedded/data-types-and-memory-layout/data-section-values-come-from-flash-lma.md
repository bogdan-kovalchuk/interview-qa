---
id: emb-dtypes-0083
title: "Що зберігає `.data` секція і звідки береться її значення при завантаженні?"
description: ".data тримає ініціалізовані глобальні, чиї початкові значення startup code копіює з Flash (LMA) у RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

`.data` зберігає **ініціалізовані глобальні та static змінні** з ненульовими значеннями.

У `.elf`: початкові значення у Flash (LMA). При boot: startup code виконує:
`memcpy(&_sdata, &_sidata, &_edata - &_sdata);`
де `_sidata` - початок даних у Flash, `_sdata`/`_edata` - границі у RAM.

Потім: `memset(&_sbss, 0, &_ebss - &_sbss);`
Потім `main()`. Контролюється linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
