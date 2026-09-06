---
id: emb-raii-0022
title: "Яка різниця між `unique_ptr` і `shared_ptr` за розміром?"
description: "unique_ptr (зі stateless deleter) зазвичай = розмір сирого вказівника; shared_ptr зазвичай = два вказівники + окремий control block."
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

**`unique_ptr` (зі stateless deleter) зазвичай = розмір сирого вказівника; `shared_ptr` зазвичай = два вказівники + окремий control block.**

`shared_ptr` зберігає вказівник на об'єкт і на control block (де лічильники), плюс сам control block у heap або в allocation, створеній `make_shared`. Точний розмір залежить від STL implementation і ABI.

Правило: один власник -> `unique_ptr`; спільний -> `shared_ptr` (платиш пам'яттю, лічильниками й часто atomics).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
