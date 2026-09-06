---
id: emb-tmplcx-0034
title: "Що має продемонструвати кандидат у питаннях про templates і constexpr?"
description: "Розуміння межі compile-time vs runtime, уміння помітити template bloat на flash-обмеженому MCU, коли CRTP кращий за virtual."
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

**Розуміння межі compile-time vs runtime, уміння помітити template bloat на flash-обмеженому MCU, коли CRTP кращий за virtual.**

Плюс: `constexpr` для перенесення обчислень у build time, `if constexpr` як типобезпечний `#ifdef`, стратегії проти bloat і перевірка через linker map.

Правило: завжди розділяй «zero runtime cost» і «реальна Flash/compile вартість».[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
