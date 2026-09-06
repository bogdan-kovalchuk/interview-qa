---
id: emb-cppstl-0020
title: "Що робить `-fno-threadsafe-statics`?"
description: "Прибирає mutex-захист навколо ініціалізації function-local static."
track: embedded
section: cpp-embedded-constraints-and-stl
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

**Прибирає mutex-захист навколо ініціалізації function-local static.**

За замовчуванням компілятор додає guard (можливо з pthread), щоб два потоки не ініціалізували static одночасно. На bare-metal без потоків це зайвий код і залежність.

Правило: `-fno-threadsafe-statics` доречний, коли немає конкурентного доступу до lazy-init static (single-threaded bare-metal).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
