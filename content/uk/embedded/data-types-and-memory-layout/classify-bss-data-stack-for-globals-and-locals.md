---
id: emb-dtypes-0028
title: "Що буде у `.bss`, `.data`, stack для: `int g1; int g2 = 5; void f(){int l=3;}`?"
description: "Неініціалізована глобальна йде у .bss, ініціалізована - у .data, а локальна змінна функції - на стек."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

`int g1;` -> **.bss** (zeroed at boot, значення 0, не займає Flash).

`int g2 = 5;` -> **.data** (значення 5 у Flash, копіюється у RAM при старті).

`int l = 3;` у функції -> **stack** (локальна, ініціалізується інструкцією при виклику функції, не zeroed автоматично, але тут є явний ініціалізатор).

Функція `f()` -> `.text` (Flash).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
