---
id: emb-structs-0046
title: "Чому `volatile` на struct pointer і `volatile` на fields не завжди одне й те саме?"
description: "Кваліфікатор має застосовуватися до того рівня типу, через який відбувається access."
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

**Кваліфікатор має застосовуватися до того рівня типу, через який відбувається access.**

`volatile GPIO_TypeDef *GPIOA` робить доступи до member-ів volatile-qualified через цей pointer. Але якщо десь отримати non-volatile alias на той самий object, доступ через нього вже не матиме volatile semantics. У CMSIS зазвичай volatile стоїть у typedef fields або access macros.

Правило: register access API має не дозволяти випадково обійти volatile-qualified шлях.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
