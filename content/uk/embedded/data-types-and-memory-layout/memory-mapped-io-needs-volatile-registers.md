---
id: emb-dtypes-0032
title: "Що таке memory-mapped I/O і навіщо `volatile` для таких регістрів?"
description: "Периферійні регістри доступні як звичайна пам'ять, а volatile забороняє компілятору кешувати чи видаляти звернення до них."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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

**Memory-mapped I/O** - периферійні регістри (GPIO, UART, ADC) доступні за фіксованими адресами у адресному просторі CPU як звичайна пам'ять.

`volatile` необхідний тому що:
1. Значення може змінитися апаратурою між читаннями (status register).
2. Без `volatile` компілятор може видалити "зайвий" запис (dead store) або кешувати значення у регістрі.

Правильно: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
