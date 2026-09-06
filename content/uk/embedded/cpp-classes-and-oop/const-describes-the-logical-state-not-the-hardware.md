---
id: emb-cppoop-0005
title: "Чому методи доступу до апаратури часто позначають `const`, хоча вони змінюють регістр?"
description: "const стосується логічного стану об'єкта, а не апаратури."
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

**`const` стосується логічного стану об'єкта, а не апаратури.**

Метод `set()` не змінює поля об'єкта `Gpio` (вказівник і pin незмінні) – він пише в апаратний регістр через них. Тому об'єкт логічно `const`, і метод можна так позначити.

Правило: const-member коректний, якщо він не модифікує members об'єкта; апаратний side effect цьому не суперечить.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
