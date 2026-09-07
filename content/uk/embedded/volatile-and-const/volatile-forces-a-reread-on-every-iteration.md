---
id: emb-volconst-0006
title: "Що зміниться після додавання `volatile`?"
description: "Компілятор мусить перечитувати rx_done з пам'яті на кожній ітерації."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
volatile uint8_t rx_done = 0;

while (rx_done == 0) { }
```

## Short answer

Компілятор мусить перечитувати `rx_done` з пам'яті на кожній ітерації.

Це дозволяє main loop побачити зміну, яку зробить ISR або DMA completion callback. Без `volatile` оптимізатор може вирішити, що значення стабільне, бо в тілі циклу немає запису в `rx_done`.

Embedded-правило: для простого ISR flag типу `uint8_t` `volatile` часто достатній для видимості, але не для складних read-modify-write сценаріїв.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
