---
id: emb-cppoop-0003
title: "Що таке неявний вказівник `this`?"
description: "Прихований параметр кожної нестатичної member-функції – адреса об'єкта, на якому її викликали."
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

**Прихований параметр кожної нестатичної member-функції – адреса об'єкта, на якому її викликали.**

`obj.set()` компілюється приблизно як виклик функції, що отримує `&obj`. Саме тому member-функція бачить поля об'єкта без префікса.

Правило: `this` робить member-функцію близькою до C-функції з явним вказівником на структуру; оптимізатор може прибрати різницю до нуля.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
