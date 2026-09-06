---
id: emb-raii-0032
title: "Чому `unique_ptr` вважають дефолтним smart pointer для embedded?"
description: "Zero overhead (як raw pointer), ексклюзивне володіння, явна передача через move, підтримка custom deleter під HAL."
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

**Zero overhead (як raw pointer), ексклюзивне володіння, явна передача через move, підтримка custom deleter під HAL.**

Він покриває переважну більшість сценаріїв володіння без витрат `shared_ptr` (control block, atomics, heap).

Правило: починай з `unique_ptr`; переходь на `shared_ptr` лише коли справді потрібне спільне володіння.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
