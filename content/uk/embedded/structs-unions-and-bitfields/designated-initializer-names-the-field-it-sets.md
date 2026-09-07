---
id: emb-structs-0029
title: "Що таке designated initializer і чому він корисний для структур?"
description: "Designated initializer явно вказує, яке поле ініціалізується: .baud = 115200."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Designated initializer** явно вказує, яке поле ініціалізується: `.baud = 115200`.

Це робить код стійкішим до зміни порядку полів і читабельнішим для configuration structs. Незаповнені поля отримують zero initialization, якщо initializer є aggregate initializer.

Embedded-правило: для driver config краще `UART_Config cfg = { .baud = 115200, .parity = PARITY_NONE };`, ніж positional initializer із довгим списком чисел.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
