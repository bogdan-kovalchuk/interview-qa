---
id: emb-volconst-0037
title: "Чому read-modify-write для volatile register може бути небезпечним?"
description: "Операція не атомарна: це читання register, модифікація в CPU, потім запис назад."
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

## Question code

```c
GPIOA_ODR |= (1u << pin);
```

## Short answer

Операція <span class="warn">не атомарна</span>: це читання register, модифікація в CPU, потім запис назад.

Якщо hardware або ISR змінить інші біти між read і write, фінальний запис може перетерти ці зміни. На Cortex-M для GPIO часто існують set/reset registers, наприклад BSRR у STM32, які дозволяють атомарно встановити або скинути біти без RMW.

Захист: для hardware registers використовуй atomic set/clear registers, bit-band там, де доступно, або critical section, якщо RMW неминучий.[^embeddedinterviewlab]

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
