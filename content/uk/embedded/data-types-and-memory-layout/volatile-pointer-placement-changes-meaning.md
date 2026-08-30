---
id: emb-dtypes-0046
title: "Що не так: `volatile int *reg` vs `int * volatile reg` - яка різниця?"
description: "volatile int *reg робить volatile дані, на які вказує reg, а int * volatile reg робить volatile сам вказівник."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

`volatile int *reg` - вказівник на **volatile int**: кожне `*reg` - реальне читання/запис (не оптимізується). Сам вказівник `reg` - не volatile. **Правильний** вибір для memory-mapped registers.

`int * volatile reg` - **volatile вказівник** на звичайний int: адреса не оптимізується, але `*reg` може бути кешований.

Для registers: `volatile uint32_t * const GPIOA = (volatile uint32_t*)0x40020000U;`[^embeddedinterviewlab]

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
