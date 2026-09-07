---
id: emb-dtypes-0051
title: "Trap: `packed struct` може спричинити HardFault на Cortex-M0 - чому?"
description: "Cortex-M0 не підтримує misaligned доступ, тож packed struct без padding може впасти у HardFault."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

Cortex-M0/M0+ <span class="warn">не підтримує misaligned memory access</span>: будь-який доступ до 2/4-байтового типу за невирівняною адресою -> <span class="warn">HardFault</span>.

`__attribute__((packed))` видаляє padding - поля можуть бути на непарних адресах. Якщо звернутись до `uint32_t` за offset 1 -> HardFault.

M3/M4 підтримують misaligned (але повільніше). Рішення: для serial/network буферів - серіалізуй/десеріалізуй через `memcpy` у вирівняний буфер.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
