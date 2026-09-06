---
id: emb-structs-0008
title: "Що перевіряє цей код?"
description: "Він перевіряє, що поле ODR у GPIO_TypeDef має offset 0x14."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
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
_Static_assert(offsetof(GPIO_TypeDef, ODR) == 0x14,
               "bad GPIO layout");
```

Він перевіряє, що поле `ODR` у `GPIO_TypeDef` має offset `0x14`.

Для peripheral struct overlay це критично: якщо попередні поля або reserved gaps описані неправильно, `GPIOA->ODR` звертатиметься не до output data register, а до іншої адреси. На Cortex-M це може означати неправильну периферію, silent bug або fault.

Правило: register maps мають мати compile-time перевірки offsets і total size.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
