---
id: emb-cppoop-0010
title: "Trap: чому залежність між глобальними об'єктами у різних `.cpp` небезпечна?"
description: "Стандарт C++ не визначає порядок конструювання глобалів між translation units (static initialization order fiasco)."
track: embedded
section: cpp-classes-and-oop
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

<span class="warn">Стандарт C++ не визначає порядок конструювання глобалів між translation units</span> (static initialization order fiasco).

Якщо глобал з `a.cpp` у своєму constructor використовує глобал з `b.cpp`, той може бути ще не сконструйований -> undefined behavior.

Захист: уникай між-модульних залежностей глобалів; використовуй function-local static (lazy init при першому виклику) або явну init-послідовність.[^embeddedinterviewlab]

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
