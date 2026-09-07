---
id: emb-dtypes-0025
title: "Як `__attribute__((packed))` впливає на `struct { char a; int b; char c; };`?"
description: "__attribute__((packed)) прибирає padding, зменшуючи розмір struct, але може викликати misaligned access."
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

Без packed: `a`@0 + 3B padding + `b`@4 + `c`@8 + 3B trailing = **12 байт**.

З `__attribute__((packed))`: `a`@0 + `b`@1 + `c`@5 = **6 байт**. Нема padding.

<span class="warn">Але!</span> На Cortex-M0/M0+ доступ до misaligned `int b` (offset 1) -> <span class="warn">HardFault</span>; На M3/M4 - повільніше; Packed корисний для serial протоколів, але не для прямого доступу до полів на MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
