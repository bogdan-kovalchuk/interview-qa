---
id: emb-volconst-0008
title: "Як правильно оголосити memory-mapped 32-bit register за адресою `0x40020014`?"
description: "Типовий варіант: #define GPIOA_ODR ((volatile uint32_t )0x40020014u)."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
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

## Short answer

Типовий варіант: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`.

Тут `volatile uint32_t *` означає pointer to volatile 32-bit data. Кожне читання або запис через macro має реально звертатися до bus address. Це важливо для GPIO, timer, UART, ADC та інших периферійних регістрів Cortex-M.

Правило: адреса peripheral register має бути явно приведена до pointer-to-volatile object; інакше оптимізатор не знає, що за адресою стоїть апаратура.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
