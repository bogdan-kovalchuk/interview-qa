---
id: emb-raii-0005
title: "Які пари HAL-функцій варто загортати в scoped handle?"
description: "Будь-яку пару acquire/release (init/deinit)."
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

**Будь-яку пару acquire/release (init/deinit).**

HAL означає hardware abstraction layer. Приклади: interrupt disable/restore, SPI (serial peripheral interface) bus lock, CS (chip select) low -> CS high, GPIO (general-purpose input/output) claim, DMA (direct memory access) channel: взяти з пулу -> повернути.

Правило: «якщо в C API (application programming interface) є парні acquire/release – обгорни їх» у RAII-об'єкт із ctor/dtor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
