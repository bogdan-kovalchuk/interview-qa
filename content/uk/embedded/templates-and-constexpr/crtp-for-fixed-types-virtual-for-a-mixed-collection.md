---
id: emb-tmplcx-0031
title: "Коли обирати CRTP, а коли virtual у шаблонному дизайні?"
description: "CRTP – фіксовані типи, performance-critical (ISR, tight loops), без virtual dispatch і vtable на об'єкт."
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

**CRTP – фіксовані типи, performance-critical (ISR, tight loops), без virtual dispatch і vtable на об'єкт.**

Virtual – потрібен runtime-поліморфізм: гетерогенні колекції, плагіни, динамічне завантаження драйверів. CRTP не дозволяє тримати різні типи в одному масиві без додаткової type-erasure обгортки.

Правило: відомі типи + швидкість -> CRTP; різні типи в runtime -> virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
