---
id: emb-dtypes-0067
title: "Що означає `-fstack-usage` у GCC і як читати його output?"
description: "-fstack-usage генерує .su файли з рядками file:line:col:function bytes type для аналізу stack frame."
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

`-fstack-usage` змушує GCC генерувати `.su` файл для кожного `.o`.

Формат: `source.c:line:col:function bytes type`
Де type: `static` (фіксований), `dynamic` (VLA/alloca), `dynamic,bounded`.

Команда аналізу: `grep -h "" *.su | sort -k2 -rn | head -20`

Доповнення: `-Wstack-usage=256` - warning для функцій >256B. Критично для bare-metal RTOS де стек кожної задачі визначений у linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
