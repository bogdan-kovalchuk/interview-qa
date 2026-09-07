---
id: emb-cppoop-0027
title: "Чи додає virtual-функцій оверхед, якщо клас узагалі їх не має?"
description: "Ні – без жодної virtual-функції клас не має ні vtable, ні vptr."
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

**Ні – без жодної virtual-функції клас не має ні vtable, ні vptr.**

`sizeof` такого об'єкта = сумі полів (+ padding), як у C-struct. Оверхед з'являється лише з першою virtual-функцією.

Правило: інкапсулюй вільно; платиш за поліморфізм, тільки коли реально оголошуєш `virtual`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
