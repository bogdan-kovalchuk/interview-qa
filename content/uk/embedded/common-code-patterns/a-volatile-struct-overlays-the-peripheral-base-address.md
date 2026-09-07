---
id: emb-patterns-0023
title: "Як описати блок регістрів периферії через struct?"
description: "Структура з volatile полями, накладена на базову адресу периферії."
track: embedded
section: common-code-patterns
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
typedef struct {
  volatile uint32_t CR;  // control
  volatile uint32_t SR;  // status
  volatile uint32_t DR;  // data
} USART_t;
#define USART1 ((USART_t *)0x40011000U)
```

## Short answer

**Структура з `volatile` полями, накладена на базову адресу периферії.**

Поля йдуть у тому ж порядку й зсувах, що й регістри в datasheet; доступ як `USART1->DR = b;`. Саме так вендорські HAL (hardware abstraction layer), наприклад STM32 HAL, NXP SDK (software development kit), TI DriverLib, визначають доступ до периферії.

Правило: фіксуй layout `offsetof`-асертами, щоб збіг із datasheet не зламався.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
