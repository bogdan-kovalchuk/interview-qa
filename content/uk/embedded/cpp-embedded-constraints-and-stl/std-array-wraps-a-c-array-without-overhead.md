---
id: emb-cppstl-0011
title: "Чим `std::array` кращий за сирий C-масив?"
description: "Zero-overhead обгортка над C-масивом з .size(), .at() (з bounds checking) і сумісністю з ."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**Zero-overhead обгортка над C-масивом з `.size()`, `.at()` (з bounds checking) і сумісністю з ``.**

Він не decay-иться у вказівник при передачі, знає свій розмір і працює з `std::sort`/`std::find`. Розмір і layout ідентичні C-масиву.

Правило: у C++ embedded `std::array` повністю заміняє `T[]` як дефолтний контейнер.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
