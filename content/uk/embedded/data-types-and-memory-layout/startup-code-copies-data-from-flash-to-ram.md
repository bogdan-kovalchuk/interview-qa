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
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
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
