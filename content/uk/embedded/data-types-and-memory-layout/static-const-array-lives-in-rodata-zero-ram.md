---
id: emb-dtypes-0068
title: "Де зберігається у функції? `static const uint16_t lookup[] = {1, 2, 3};`"
description: "static const кладе масив у .rodata у Flash, тож він не витрачає жодного байта RAM."
track: embedded
section: data-types-and-memory-layout
level: junior
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

У секції **.rodata** (Flash). Комбінація `static const`: `static` -> не на стеку (статична тривалість); `const` -> read-only.

Результат: дані у Flash, **нуль RAM витрат**.

Якби `static uint16_t lookup[] = {1,2,3};` (без `const`) -> `.data` (RAM + Flash copy at boot).

Правило: для lookup tables, calibration data, string tables - завжди `static const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
