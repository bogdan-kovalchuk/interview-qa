---
id: emb-cppoop-0024
title: "Які переваги композиції в embedded?"
description: "Передбачуваний розмір, гнучка підміна, слабке зчеплення."
track: embedded
section: cpp-classes-and-oop
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

**Передбачуваний розмір, гнучка підміна, слабке зчеплення.**

Розмір кожного компонента самодостатній і відомий; компоненти можна міняти на етапі компіляції (templates) або в runtime (вказівники); зміни base не каскадять по дереву успадкування.

Правило: композиція за замовчуванням робить модулі незалежно тестованими й стабільними до змін.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
