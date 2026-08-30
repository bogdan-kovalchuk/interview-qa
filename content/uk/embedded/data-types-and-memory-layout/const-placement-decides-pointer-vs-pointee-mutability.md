---
id: emb-dtypes-0059
title: "Що означає `const` у `const uint32_t *p` vs `uint32_t * const p`?"
description: "const перед типом захищає дані, на які вказує вказівник, а const після * захищає саму адресу."
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

`const uint32_t *p` - вказівник на **константний uint32_t**: не можна змінити `*p`, але можна змінити `p` (вказувати на інше місце).

`uint32_t * const p` - **константний вказівник**: адреса фіксована, але `*p` можна змінити.

`const uint32_t * const p` - і дані, і адреса незмінні.

Правило: читай справа наліво. Для registers: `volatile uint32_t * const REG = (volatile uint32_t*)0x40020000U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
