---
id: emb-raii-0027
title: "Чому RAII-guard роблять `explicit` у конструкторі?"
description: "Щоб заборонити неявне перетворення з handle у guard."
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

**Щоб заборонити неявне перетворення з handle у guard.**

`explicit LockGuard(osMutexId_t)` не дає випадково створити тимчасовий guard через implicit conversion (наприклад, при передачі мьютекса у функцію), що могло б захопити/звільнити lock у несподіваний момент.

Правило: конструктори-обгортки з одним аргументом роби `explicit`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
