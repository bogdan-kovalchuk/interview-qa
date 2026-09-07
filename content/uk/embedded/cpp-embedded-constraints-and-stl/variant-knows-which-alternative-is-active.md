---
id: emb-cppstl-0032
title: "Що таке `std::variant` і чим він кращий за union?"
description: "Type-safe union (C++17): знає, який саме тип зараз активний, і не дає прочитати інший."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Type-safe union (C++17): знає, який саме тип зараз активний, і не дає прочитати інший.**

Сирий `union` не відстежує активний член – читання «не того» поля це UB (undefined behavior). `std::variant` + `std::visit` роблять це безпечно, без heap.

Захист: visitor має покривати всі альтернативи; некоректний visitor зазвичай ловиться на компіляції, а не в runtime.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
