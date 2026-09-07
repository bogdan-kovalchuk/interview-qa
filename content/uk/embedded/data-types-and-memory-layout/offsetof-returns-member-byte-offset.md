---
id: emb-dtypes-0054
title: "Навіщо потрібен `offsetof()` і де він визначений?"
description: "offsetof(type, member) повертає зміщення поля від початку структури і визначений у stddef.h."
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

`offsetof(type, member)` повертає зміщення поля від початку структури у байтах. Визначений у `<stddef.h>`.

Використання:
1. Compile-time перевірка layout: `static_assert(offsetof(CanFrame, crc) == 6, "Wrong layout");`
2. Серіалізація/десеріалізація;
3. **container_of** macro (Linux kernel) - отримати struct* за member*.

Критично для binary protocol та hardware register mapping.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
