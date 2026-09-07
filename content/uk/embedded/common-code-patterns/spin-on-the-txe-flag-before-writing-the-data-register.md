---
id: emb-patterns-0026
title: "Як коректно чекати прапорець TXE перед записом у UART (universal asynchronous receiver-transmitter)?"
description: "Спін на бітовому тесті статус-регістра, потім запис у data-регістр."
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
void usart1_send(uint8_t b) {
  while (!(USART1->SR & BIT(7))) // wait TXE
    ;
  USART1->DR = b;
}
```

## Short answer

**Спін на бітовому тесті статус-регістра, потім запис у data-регістр.**

Працює лише з `volatile` полями (інакше нескінченний цикл). `BIT(7)` – маска TXE (transmit data register empty); коли FIFO/TX (first-in, first-out / transmit) готовий, біт виставляється апаратурою.

Правило: poll -> перевір прапорець готовності -> дій; для довгих очікувань додавай timeout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
