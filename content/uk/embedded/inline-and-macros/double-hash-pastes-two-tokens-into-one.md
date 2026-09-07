---
id: emb-macros-0013
title: "Що робить оператор склеювання токенів `##`?"
description: "## з'єднує два токени в один на етапі препроцесингу: GPIOA + _ + ODR -> ідентифікатор GPIOA_ODR."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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
#define REG(periph, r) periph##_##r
// REG(GPIOA, ODR) -> GPIOA_ODR
```

## Short answer

**`##` з'єднує два токени в один** на етапі препроцесингу: `GPIOA` + `_` + `ODR` -> ідентифікатор `GPIOA_ODR`.

Використовується для генерації імен регістрів, функцій-обгорток, unique-ідентифікаторів і X-macro патернів.

Правило: результат склеювання має бути валідним токеном; інакше – помилка препроцесора.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
