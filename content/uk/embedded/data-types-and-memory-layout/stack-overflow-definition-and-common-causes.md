---
id: emb-dtypes-0029
title: "Що таке stack overflow і які його причини в embedded?"
description: "Stack overflow - це перевищення розміру стека, найчастіше через великі локальні масиви або глибоку рекурсію."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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

Stack overflow - перевищення розміру стека -> перезапис сусідніх областей пам'яті (`.bss`, heap, інший стек).

Причини:
1. **Великі локальні масиви**: `uint8_t buf[2048]` на стеку;
2. Глибока рекурсія;
3. Вкладені ISR (кожен займає ≥8B для exception frame на Cortex-M);
4. Замалий стек у linker script.

Діагностика: stack canaries, `-fstack-usage`, MPU protection, заповнення стека патерном `0xDEAD`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
