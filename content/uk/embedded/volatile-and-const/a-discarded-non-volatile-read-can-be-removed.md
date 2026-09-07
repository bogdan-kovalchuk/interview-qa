---
id: emb-volconst-0036
title: "Trap: що не так із читанням register без використання результату?"
description: "Якщо macro не volatile, компілятор може прибрати це читання."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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
#define ADC_DR (*( uint32_t *)0x4001204C)

ADC_DR;
```

## Short answer

<span class="warn">Якщо macro не volatile, компілятор може прибрати це читання.</span>

Для data register читання може очищати апаратний flag або витягувати sample з FIFO. Але для звичайного `uint32_t` expression statement без використання результату не має observable effect, тому оптимізатор має право його видалити.

Захист: register macro має бути `(*(volatile uint32_t *)address)`. Якщо читання навмисне discard-иться, іноді додають явний cast `(void)ADC_DR` для читабельності.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
