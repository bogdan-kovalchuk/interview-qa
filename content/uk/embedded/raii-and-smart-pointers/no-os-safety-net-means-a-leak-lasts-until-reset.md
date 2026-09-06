---
id: emb-raii-0002
title: "Чому RAII критичний саме в embedded?"
description: "Немає OS (operating system) страхувальної сітки й garbage collector – забутий ресурс може лишитися зайнятим до reset."
track: embedded
section: raii-and-smart-pointers
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

**Немає OS (operating system) страхувальної сітки й garbage collector – забутий ресурс може лишитися зайнятим до reset.**

Забутий `mutex_unlock()` -> постійний deadlock; незакритий DMA (direct memory access) канал стає недоступним до перезавантаження. На десктопі ОС прибере за процесом, на MCU (microcontroller unit) – часто ні.

Правило: у embedded RAII не «зручність», а захист від цілого класу фатальних leak'ів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
