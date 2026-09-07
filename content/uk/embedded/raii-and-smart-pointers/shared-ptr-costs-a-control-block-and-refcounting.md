---
id: emb-raii-0010
title: "Чому `shared_ptr` рідко використовують у embedded?"
description: "Дорогий: control block на об'єкт, reference counting на copy/assign/destroy і зазвичай heap allocation."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Дорогий: control block на об'єкт, reference counting на copy/assign/destroy і зазвичай heap allocation.</span>

Розмір control block implementation-defined, але це точно не «один pointer». Плюс недетермінізм: очищення стається лише коли знищено останнього власника, і не завжди очевидно, де саме це відбудеться.

Правило: на bare-metal без heap уникай `shared_ptr`; для одного власника бери `unique_ptr`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
