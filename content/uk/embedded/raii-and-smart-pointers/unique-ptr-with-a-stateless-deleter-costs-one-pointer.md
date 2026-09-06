---
id: emb-raii-0008
title: "Який оверхед у `unique_ptr` порівняно з сирим вказівником?"
description: "Зі stateless deleter unique_ptr зазвичай має розмір одного raw pointer-а."
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

**Зі stateless deleter `unique_ptr` зазвичай має розмір одного raw pointer-а.**

Немає control block, немає ref counting. Deleter type відомий на compile time, тому компілятор часто інлайнить виклик teardown. Якщо deleter має стан або є function pointer, `sizeof(unique_ptr)` може зрости.

Правило: `unique_ptr` – дефолтний smart pointer в embedded; для нульового size overhead тримай deleter stateless.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
