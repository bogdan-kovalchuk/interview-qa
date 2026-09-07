---
id: emb-cppoop-0021
title: "CRTP vs virtual: коли що обирати?"
description: "Virtual – гетерогенні колекції (масив Base з різними типами), dispatch у runtime, одна копія base-коду."
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

**Virtual** – гетерогенні колекції (масив `Base*` з різними типами), dispatch у runtime, одна копія base-коду.

CRTP (Curiously Recurring Template Pattern) – фіксовані типи, performance-critical: compile-time dispatch, без vtable/vptr, передбачувані прямі виклики. Ціна – дублювання base-коду на кожен похідний тип.

Правило: різні типи в одному контейнері -> virtual; максимальна швидкість при відомих типах -> CRTP.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
