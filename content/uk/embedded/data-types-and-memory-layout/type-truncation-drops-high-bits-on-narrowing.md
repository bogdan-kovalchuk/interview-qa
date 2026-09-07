---
id: emb-dtypes-0039
title: "Що таке type truncation і коли він виникає?"
description: "Type truncation відкидає старші біти при присвоєнні ширшого типу вужчому, наприклад int у uint8_t."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

**Type truncation** - відкидання старших біт при присвоєнні ширшого типу вужчому.

Приклад: `int x = 300; uint8_t y = x;` -> `300 = 0x012C`, відкидаємо `0x01`, лишається `0x2C = 44`.

Виникає: при присвоєнні, при поверненні з функції, при передачі аргументу меншого типу. Implicit truncation часто не генерує warning без `-Wall -Wconversion`. Завжди перевіряй діапазон перед звуженням.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
