---
id: emb-raii-0011
title: "Які конкретні витрати має `shared_ptr`?"
description: "Control block, reference counters, зазвичай atomic increments/decrements, heap allocation і недетермінований момент очищення."
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

**Control block, reference counters, зазвичай atomic increments/decrements, heap allocation і недетермінований момент очищення.**

Типовий `shared_ptr` сам містить два pointer-и: pointer на object і pointer на control block. Control block зберігає strong/weak counters і deleter/allocator state. `make_shared` зменшує кількість алокацій, але не прибирає control block.

Правило: на інтерв'ю називай категорії витрат, а не лише «shared_ptr повільний».[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
