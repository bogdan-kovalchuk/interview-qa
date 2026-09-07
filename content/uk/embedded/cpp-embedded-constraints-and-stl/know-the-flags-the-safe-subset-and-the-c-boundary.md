---
id: emb-cppstl-0035
title: "Що має продемонструвати кандидат про C++ constraints і STL в embedded?"
description: "Чому вимикають exceptions/RTTI, яка безпечна STL-підмножина, як працює extern \"C\", placement new, що зазвичай обмежує MISRA C++."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 3
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

**Чому вимикають exceptions/RTTI, яка безпечна STL-підмножина, як працює `extern "C"`, placement new, що зазвичай обмежує MISRA C++.**

Плюс: `std::array` як дефолтний контейнер, `std::optional`/`std::string_view` замість null/`std::string`, і що C++ дає zero-cost абстракції (не «важкий для embedded»).

Правило: показуй конкретні прапорці, конкретні заміни контейнерів і конкретні стандарти.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
