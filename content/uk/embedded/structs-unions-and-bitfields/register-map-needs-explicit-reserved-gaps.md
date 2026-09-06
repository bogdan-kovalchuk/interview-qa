---
id: emb-structs-0009
title: "Trap: що не так із таким register map?"
description: "Можуть бракувати reserved gaps між регістрами."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
typedef struct {
    volatile uint32_t CR;
    volatile uint32_t SR;
    volatile uint32_t DR;
} UART_TypeDef;
```

Можуть бракувати reserved gaps між регістрами.

Hardware register map часто має пропуски адрес. Якщо manual каже, що `DR` на offset `0x10`, а структура ставить його на offset `0x08`, усі доступи після gap будуть неправильними. `volatile` не рятує неправильний layout.

Захист: додавай reserved поля потрібного розміру, наприклад `uint32_t RESERVED0[2]`, і перевіряй `offsetof`.[^embeddedinterviewlab]

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
