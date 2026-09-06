---
id: emb-cppoop-0002
title: "Чим `class` відрізняється від `struct` у C++?"
description: "Головна відмінність – доступ за замовчуванням: class – private, struct – public."
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

**Головна відмінність – доступ за замовчуванням: `class` – private, `struct` – public.**

Також default inheritance різний: `class Derived : Base` успадковує private, а `struct Derived : Base` – public. В іншому вони однаково можуть мати методи, конструктори, успадкування.

Правило: за конвенцією `struct` – для простих POD-like (plain old data) агрегатів, `class` – коли є інваріанти й інкапсуляція.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
