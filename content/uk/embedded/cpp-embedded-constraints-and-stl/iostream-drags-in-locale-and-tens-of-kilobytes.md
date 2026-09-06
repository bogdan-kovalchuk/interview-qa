---
id: emb-cppstl-0027
title: "Чому в embedded уникають `<iostream>` на користь `printf`?"
description: "<iostream> може тягнути locale, heap-буфери, глобальну ініціалізацію й десятки КБ Flash."
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

`<iostream>` може тягнути locale, heap-буфери, глобальну ініціалізацію й десятки КБ Flash.

`std::cout` ініціалізує важку інфраструктуру ще до `main()`; на MCU це часто неприйнятно. `printf` (особливо урізаний/nano) або власний trace backend зазвичай значно легші.

Правило: для логів на MCU – `printf`/власний trace backend, не `iostream`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
