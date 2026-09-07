---
id: emb-volconst-0055
title: "Trap: що не так із таким оголошенням register address?"
description: "Це створює окрему volatile-змінну і лише ініціалізує її значенням register-а."
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
volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;
```

## Short answer

<span class="warn">Це створює окрему volatile-змінну і лише ініціалізує її значенням register-а.</span>

Після ініціалізації `GPIOA_ODR` не є alias на address `0x40020014`; це object у RAM або іншій секції. Запис у `GPIOA_ODR` не запише hardware register.

Захист: використовуй macro/lvalue або pointer: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)` чи `volatile uint32_t * const GPIOA_ODR = ...`.[^embeddedinterviewlab]

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
