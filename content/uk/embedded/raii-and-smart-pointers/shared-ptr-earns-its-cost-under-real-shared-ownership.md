---
id: emb-raii-0012
title: "Коли `shared_ptr` все ж виправданий у embedded?"
description: "Коли є справжнє спільне володіння і доступні heap + atomics."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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

**Коли є справжнє спільне володіння і доступні heap + atomics.**

Приклади: reference-counted buffers у embedded Linux userspace, plugin/модульні системи зі спільними config-блоками, об'єкти з lifetime, який справді не має одного власника. Для DMA (direct memory access) buffers у bare-metal частіше краще явний owner + borrowed views.

Правило: `shared_ptr` – лише для реального shared ownership, не «про всяк випадок».[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
