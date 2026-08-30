---
id: emb-dtypes-0089
title: "Що таке type punning і коли це undefined behavior у C++?"
description: "У C type punning через union прийнятний, а у C++ безпечний лише через memcpy або std::bit_cast."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

**Type punning** - читання об'єкта одного типу через pointer/reference іншого типу.

У **C**: через `union` - поширений і підтримуваний прийом, але результат залежить від представлення типів у пам'яті.
Через cast pointer: `int x = 1; float *fp = (float*)&x; *fp;` - <span class="warn">UB (strict aliasing violation)</span>.

У **C++**: лише `memcpy` або `std::bit_cast` (C++20) - безпечний type punning. `reinterpret_cast` + dereference -> UB.

Компілятор оптимізує код припускаючи aliasing не відбувається.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
