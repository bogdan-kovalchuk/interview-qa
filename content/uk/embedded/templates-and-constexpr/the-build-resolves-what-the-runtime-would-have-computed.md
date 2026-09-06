---
id: emb-tmplcx-0026
title: "Що означає «zero-cost abstraction» для templates і constexpr?"
description: "Компілятор резолвить типи й рахує значення на етапі білду – після оптимізації код може бути таким самим щільним, як ручний C, але з сильнішою типобезпекою."
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

**Компілятор резолвить типи й рахує значення на етапі білду – після оптимізації код може бути таким самим щільним, як ручний C, але з сильнішою типобезпекою.**

Важливо: це стосується runtime-вартості правильно спроєктованої абстракції; flash footprint і час компіляції мають реальну ціну.

Правило: zero-cost = немає обов'язкової runtime-ціни, але не «безкоштовно» у Flash і build time.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
