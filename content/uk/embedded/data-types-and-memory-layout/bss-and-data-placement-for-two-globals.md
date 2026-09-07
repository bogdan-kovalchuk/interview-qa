---
id: emb-dtypes-0008
title: "Визначте секцію пам'яті: `uint32_t error_count;` (глобальна) та `uint32_t sensor_count = 5;` (глобальна)"
description: "Неініціалізована глобальна йде у .bss, а ініціалізована ненульовим значенням - у .data."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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

`uint32_t error_count;` -> **.bss**: не ініціалізована глобальна, zeroed at boot, не займає Flash.

`uint32_t sensor_count = 5;` -> **.data**: ініціалізована глобальна, значення `5` зберігається у Flash і копіюється у RAM при завантаженні.

Обидві живуть весь час виконання програми.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
