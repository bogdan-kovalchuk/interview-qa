---
id: emb-dtypes-0060
title: "Як `calloc` відрізняється від `malloc` в контексті ініціалізації пам'яті?"
description: "malloc виділяє пам'ять без ініціалізації, а calloc виділяє і одразу заповнює нулями."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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

`malloc(size)` виділяє `size` байт і <span class="warn">НЕ ініціалізує</span> (garbage), тоді як `calloc(n, size)` виділяє `n × size` байт і **заповнює нулями**, додатково перевіряючи переповнення добутку.

Обидва повертають `NULL` при помилці. У embedded надавай перевагу static allocation; якщо вже heap - `calloc` безпечніший для структур де потрібна нульова ініціалізація.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
