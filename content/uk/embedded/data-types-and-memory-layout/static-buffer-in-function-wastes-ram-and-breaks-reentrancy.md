---
id: emb-dtypes-0076
title: "Trap у embedded - які ризики? `static uint8_t buffer[4096];`"
description: "static буфер у функції живе в .bss увесь час, займає RAM назавжди і ламає reentrancy."
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

`static` у функції -> буфер у `.bss` (RAM, zeroed at boot). 4096B може бути критичною частиною RAM (20% від 20KB!).

Ризики:
1. <span class="warn">Функція не reentrant</span> - ISR і main loop поділяють буфер;
2. Займає RAM весь час (навіть коли не використовується);
3. Якщо у кількох функціях - RAM швидко вичерпується;
4. Статичний аналіз не завжди виявляє overlap.

Альтернатива: один глобальний буфер + mutex, або memory pool.[^embeddedinterviewlab]

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
