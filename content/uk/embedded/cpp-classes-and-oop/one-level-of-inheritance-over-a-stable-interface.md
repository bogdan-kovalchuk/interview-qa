---
id: emb-cppoop-0012
title: "Коли успадкування доречне в embedded, а коли – ні?"
description: "Доречне: один рівень глибини (base-інтерфейс + конкретні реалізації), мало типів (2–5), стабільний інтерфейс."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

**Доречне**: один рівень глибини (base-інтерфейс + конкретні реалізації), мало типів (2–5), стабільний інтерфейс.

<span class="warn">Уникай</span>: глибокі ієрархії (3+ рівні) -> крихке зчеплення; часті зміни інтерфейсу каскадять по дереву; тісний ROM-бюджет, де vtable-оверхед має значення.

Правило: один рівень абстракції – успадкування; усе інше – композиція.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
