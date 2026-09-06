---
id: emb-structs-0004
title: "Як зменшити padding у структурі без `packed`?"
description: "Розташувати поля від найбільшого alignment до найменшого."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Розташувати поля від найбільшого alignment до найменшого**.

Наприклад, замість `uint8_t, uint32_t, uint8_t` краще `uint32_t, uint8_t, uint8_t`. Це не змінює semantics, якщо структура не є зовнішнім ABI/wire-format контрактом, але може суттєво зменшити розмір масиву структур.

Правило: для internal data structures оптимізуй порядок полів; для protocol/register layout порядок має відповідати специфікації, навіть якщо є padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
