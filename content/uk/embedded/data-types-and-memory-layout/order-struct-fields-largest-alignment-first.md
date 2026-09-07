---
id: emb-dtypes-0084
title: "Чому рекомендується розташовувати поля структури від більших до менших?"
description: "Сортування полів від більшого вирівнювання до меншого мінімізує внутрішній padding structа."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Сортування від більшого alignment до меншого **мінімізує внутрішній padding**.

Поганий порядок: `struct { char a; int b; char c; }` -> 12B (3B + 3B padding).
Хороший порядок: `struct { int b; char a; char c; }` -> 8B (нема внутрішнього padding).

Правило: спочатку `uint64_t`/`double` (align 8), потім `uint32_t`/`float` (align 4), потім `uint16_t` (align 2), нарешті `uint8_t`/`char` (align 1). Перевіряй `sizeof()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
