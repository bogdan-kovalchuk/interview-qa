---
id: emb-dtypes-0098
title: "Що відбудеться: `uint32_t *ptr = (uint32_t*)0x40020000; *ptr = 0xFF;` без `volatile`?"
description: "Без volatile компілятор може видалити запис як dead store, бо ніхто далі не читає *ptr."
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

Компілятор може <span class="warn">видалити запис як dead store</span> (dead store elimination): ніде далі `*ptr` не читається у програмному потоці, тому компілятор вважає запис "зайвим".

Без `volatile` - <span class="warn">нема гарантії</span> що байти реально потраплять до GPIO.

Правильно: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;` - кожен запис/читання реально виконується.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
