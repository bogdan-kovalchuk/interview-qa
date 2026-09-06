---
id: emb-cppoop-0018
title: "Як virtual dispatch шкодить детермінізму на простих ядрах?"
description: "Virtual call – це indirect branch через vptr/vtable, тому ціль виклику не видно напряму з інструкції."
track: embedded
section: cpp-classes-and-oop
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

**Virtual call – це indirect branch через vptr/vtable, тому ціль виклику не видно напряму з інструкції.**

На простих Cortex-M це додаткове читання pointer-а і indirect branch; на складніших ядрах це також може погіршити branch prediction. Головна проблема для safety/real-time – складніше довести worst-case execution time і call graph.

Правило: AUTOSAR (Automotive Open System Architecture) C++14 і MISRA C++ (Motor Industry Software Reliability Association C++) обмежують virtual dispatch у time-critical шляхах; у hot path часто обирають CRTP або templates.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
