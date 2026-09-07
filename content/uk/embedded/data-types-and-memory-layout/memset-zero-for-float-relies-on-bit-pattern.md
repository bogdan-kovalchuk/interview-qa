---
id: emb-dtypes-0061
title: "Що не так: `memset(ptr, 0, sizeof(*ptr))` для ініціалізації `float`-поля у struct?"
description: "memset покладається на те, що нуль-байти дають float 0.0f, а стандарт C формально цього не гарантує."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

Формально: `memset` встановлює всі байти в 0. IEEE 754 `0.0f` = bit pattern `0x00000000` -> на практиці працює.

Але: стандарт C не гарантує що float нуль = всі байти нуль (теоретично). Більша проблема: `memset(struct_ptr, 0, sizeof(*struct_ptr))` для struct з `void*` - <span class="warn">NULL pointer</span> не гарантовано bit-pattern 0x0 за стандартом (хоча практично так).

Краща практика: явна ініціалізація кожного поля.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
