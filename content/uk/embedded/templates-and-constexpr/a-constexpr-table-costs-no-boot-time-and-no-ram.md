---
id: emb-tmplcx-0033
title: "Чому constexpr-таблиця у Flash краща за обчислення таблиці при старті?"
description: "Вона не марнує boot time й RAM – готова константа лежить у .rodata."
track: embedded
section: templates-and-constexpr
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

**Вона не марнує boot time й RAM – готова константа лежить у `.rodata`.**

Startup-цикл, що рахує CRC (cyclic redundancy check) або іншу lookup-таблицю, додає затримку до `main()` і часто тримає таблицю в RAM. `constexpr` переносить це у build time, лишаючи RAM вільною.

Правило: незмінні похідні дані обчислюй на компіляції, а не в startup-коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
