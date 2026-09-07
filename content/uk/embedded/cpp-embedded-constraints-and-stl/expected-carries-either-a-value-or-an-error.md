---
id: emb-cppstl-0005
title: "Що таке `std::expected<T, E>` і чим замінити його до C++23?"
description: "Тип, що несе АБО значення, АБО помилку, і робить перевірку результату явною в типі."
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

**Тип, що несе АБО значення, АБО помилку, і робить перевірку результату явною в типі.**

До C++23 пишуть власний легкий `Result<T, E>` без heap-алокації – невеликий клас із прапорцем «успіх/помилка» та union-подібним сховищем.

Правило: `expected`/`Result` поєднує значення й помилку в одному типі без винятків і без купи.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
