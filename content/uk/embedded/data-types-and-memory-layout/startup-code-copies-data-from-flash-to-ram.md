---
id: emb-dtypes-0038
title: "Що зробить startup code з секцією `.data` перед викликом `main()`?"
description: "Startup code копіює початкові значення .data з Flash (LMA) у RAM (VMA) перед запуском main()."
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

Startup code копіює початкові значення `.data` з Flash (LMA - Load Memory Address) у RAM (VMA - Virtual Memory Address).

Приклад: `uint32_t x = 42;` -> у Flash байти `{0x2A,0x00,0x00,0x00}`, startup code копіює їх у RAM. Тоді `x` у RAM = 42.

Імплементація (startup.s): `memcpy(&_sdata, &_sidata, &_edata - &_sdata);`. Далі: `memset(&_sbss, 0, &_ebss - &_sbss);`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
