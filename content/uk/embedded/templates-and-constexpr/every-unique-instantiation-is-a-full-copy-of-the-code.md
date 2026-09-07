---
id: emb-tmplcx-0014
title: "Звідки береться code bloat від шаблонів?"
description: "Кожна унікальна інстанціація = окрема повна копія коду у Flash."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Кожна унікальна інстанціація = окрема повна копія коду у Flash.</span>

`CircularBuffer<uint8_t,64>`, `<uint16_t,64>`, `<uint32_t,64>` дадуть три повні копії всіх методів, хоча логіка однакова.

Правило: стеж за кількістю інстанціацій – на flash-обмежених MCU це швидко з'їдає ROM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
