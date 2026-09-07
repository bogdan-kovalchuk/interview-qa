---
id: emb-cppstl-0031
title: "Trap: чому сирий C-масив у C++-сигнатурі – поганий сигнал на інтерв'ю?"
description: "Він decay-иться у вказівник (втрата розміру) і показує незнання сучасних практик."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
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

<span class="warn">Він decay-иться у вказівник (втрата розміру) і показує незнання сучасних практик.</span>

`void f(int arr[])` насправді приймає `int*`; `sizeof` усередині дасть розмір вказівника. `std::array`/`std::span` зберігають розмір і безпечніші.

Захист: у C++ передавай `std::array&`, `std::span` або (контейнер + розмір), а не голий `T[]`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
