---
id: emb-macros-0037
title: "Як через макрос задати доступ до memory-mapped регістра?"
description: "Макрос розгортається у lvalue-доступ до фіксованої адреси, тому можна писати GPIOA_ODR = 0xFF; і x = GPIOA_ODR;."
track: embedded
section: inline-and-macros
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
#define GPIOA_ODR \
  (*(volatile uint32_t *)0x40020014U)
```

## Short answer

**Макрос розгортається у lvalue-доступ до фіксованої адреси**, тому можна писати `GPIOA_ODR = 0xFF;` і `x = GPIOA_ODR;`.

`volatile` забороняє компілятору кешувати чи викидати доступ; cast перетворює числову адресу на типізований вказівник; зовнішня `*` розіменовує. Суфікс `U` робить літерал unsigned.

Правило: це один із випадків, де макрос виправданий – функцією таку адресну константу зручно не виразиш.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
