---
id: emb-cppstl-0006
title: "Які стратегії виділення пам'яті використовують замість heap?"
description: "Static allocation, placement new, fixed-size memory pools, stack allocation."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Static allocation, placement new, fixed-size memory pools, stack allocation.**

Усі об'єкти мають static/automatic storage; немає `new`/`delete`. Pool дає O(1) без фрагментації; стек – для локальних, але невеликих (стеки 1–4 КБ).

Правило: у безпеко-критичному embedded heap або заборонений, або лише на етапі ініціалізації.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
