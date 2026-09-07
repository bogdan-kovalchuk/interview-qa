---
id: emb-dtypes-0037
title: "Яка різниця між `uint32_t` та `unsigned int` у контексті portability?"
description: "unsigned int залежить від платформи, а uint32_t завжди рівно 32 біти на будь-якій платформі."
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

`unsigned int` - platform-dependent: 2 байти на 16-bit MCU, 4 байти на 32-bit.

`uint32_t` - **завжди рівно 32 біти** на будь-якій платформі (визначений у `<stdint.h>`).

У embedded: register maps, протоколи, struct layout -> завжди `uint32_t`. Для розмірів та індексів -> `size_t`. `unsigned int` доцільний лише якщо конкретний розмір не критичний.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
