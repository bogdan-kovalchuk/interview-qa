---
id: emb-dtypes-0010
title: "Який розмір матиме на 32-bit Cortex-M? `struct { char c; int x; };`"
description: "Компілятор вставляє padding перед int, щоб struct { char; int; } займала 8, а не 5 байт."
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

**8 байт** (не 5!).

Layout: `char c` @ offset 0 (1B) -> <span class="warn">3 байти padding</span> -> `int x` @ offset 4 (4B). Trailing padding = 0.

Padding вставляється щоб `int` був на адресі кратній 4 (alignment вимога). Перевіряй: `offsetof(s, x) == 4`; Завжди використовуй `sizeof()` та `offsetof()` для аналізу layout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
