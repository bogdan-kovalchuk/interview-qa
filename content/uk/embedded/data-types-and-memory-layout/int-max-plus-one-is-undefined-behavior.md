---
id: emb-dtypes-0091
title: "Trap: що відбудеться за стандартом C? `int x = INT_MAX; x++;`"
description: "Переповнення signed int за INT_MAX - undefined behavior, а не гарантований wraparound до INT_MIN."
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

<span class="warn">Signed integer overflow -> undefined behavior</span> (C §6.5).

Компілятор може:
1. Зробити wraparound до `INT_MIN` (типово на x86/ARM two's complement);
2. Оптимізувати код неочікуваним чином (наприклад, видалити умовний захисний код);
3. Нескінченний цикл у певних патернах.

Для визначеного wraparound: `uint32_t x = UINT32_MAX; x++;` -> `0`.
Перевірка: `if(x < INT_MAX) x++;`[^embeddedinterviewlab]

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
