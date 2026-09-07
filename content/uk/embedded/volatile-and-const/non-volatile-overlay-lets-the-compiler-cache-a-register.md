---
id: emb-volconst-0046
title: "Trap: що не так із таким struct overlay?"
description: "Поля register overlay не volatile-qualified."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

```c
typedef struct {
    uint32_t MODER;
    uint32_t IDR;
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
```

<span class="warn">Поля register overlay не volatile-qualified.</span>

`GPIOA->IDR` має тип звичайного `uint32_t`, тому compiler може кешувати або оптимізувати доступ. Для peripheral registers це неправильно, бо hardware може змінювати IDR незалежно від C-коду.

Захист: оголоси поля як `volatile uint32_t MODER;`, `volatile uint32_t IDR;` або використовуй vendor CMSIS headers, де qualifiers уже задані.[^embeddedinterviewlab]

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
