---
id: emb-cppstl-0026
title: "Trap: чому казати «C++ занадто важкий для embedded» – погана відповідь?"
description: "Це демонструє незнання zero-cost abstractions і реальних важелів контролю runtime."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
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

Це демонструє незнання zero-cost abstractions і реальних важелів контролю runtime.

Non-virtual класи, templates, `constexpr`, RAII (resource acquisition is initialization) можуть компілюватися без додаткового runtime-оверхеду, якщо вимкнути/уникати важких фіч і перевіряти map-файл. Реальна ціна залежить від ABI, стандартної бібліотеки й оптимізацій.

Захист: говори конкретно – що саме вимикаєш (`-fno-exceptions`/`-fno-rtti`) і яку підмножину STL береш.[^embeddedinterviewlab]

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
