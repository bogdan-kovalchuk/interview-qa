---
id: emb-cppoop-0033
title: "Що таке encapsulation і яку гарантію він дає в драйвері?"
description: "Приховування внутрішнього стану за публічним інтерфейсом, щоб інваріанти не можна було порушити ззовні."
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

**Приховування внутрішнього стану за публічним інтерфейсом**, щоб інваріанти не можна було порушити ззовні.

Драйвер тримає регістри/буфери private і відкриває лише валідовані операції; це не коштує runtime (поки без virtual) і робить неможливими цілі класи багів (сирий доступ повз перевірки).

Правило: інкапсуляція в embedded C++ – безкоштовна безпека, а не «академічна» розкіш.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
