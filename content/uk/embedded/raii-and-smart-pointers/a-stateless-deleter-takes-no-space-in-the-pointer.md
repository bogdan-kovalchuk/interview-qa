---
id: emb-raii-0023
title: "Чому custom deleter варто робити stateless?"
description: "Stateless deleter type (лямбда без capture або empty functor) може не займати місця в unique_ptr завдяки empty base optimization."
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

**Stateless deleter type (лямбда без capture або empty functor) може не займати місця в `unique_ptr` завдяки empty base optimization.**

Capturing-лямбда несе стан, тож збільшує `sizeof(unique_ptr)` і може завадити оптимізації. Function pointer deleter теж не має object state, але сам pointer треба зберігати в `unique_ptr`, тому розмір зазвичай стає два pointer-и.

Правило: deleter без runtime state -> `unique_ptr` може лишатися завбільшки з raw pointer; function pointer deleter – простий, але не size-free.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
