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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

`malloc(size)` - виділяє `size` байт, <span class="warn">НЕ ініціалізує</span> (garbage).

`calloc(n, size)` - виділяє `n × size` байт, **заповнює нулями**. Додатково перевіряє переповнення добутку `n × size`.

Обидва повертають `NULL` при помилці. У embedded: надавай перевагу static allocation. Якщо вже heap - `calloc` безпечніший для структур де потрібна нульова ініціалізація.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
