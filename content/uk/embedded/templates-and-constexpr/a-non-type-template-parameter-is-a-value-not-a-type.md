---
id: emb-tmplcx-0004
title: "Що таке non-type template parameter (NTTP)?"
description: "Параметр шаблону, який є значенням (а не типом) – напр."
track: embedded
section: templates-and-constexpr
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

**Параметр шаблону, який є значенням (а не типом) – напр. `size_t N`.**

У `CircularBuffer<T, N>` розмір `N` – NTTP: компілятор знає його на етапі білду, тож може виділити масив фіксованого розміру і згорнути обчислення в константи.

Правило: NTTP дозволяє «зашити» розміри/конфігурацію в тип і отримати compile-time перевірки меж.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
