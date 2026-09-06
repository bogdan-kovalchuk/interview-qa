---
id: emb-cppstl-0003
title: "Чому вимикають RTTI (`-fno-rtti`) і що це забирає?"
description: "RTTI (run-time type information) зберігає метадані типу на клас у Flash; вимкнення економить ROM."
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

**RTTI (run-time type information) зберігає метадані типу на клас у Flash; вимкнення економить ROM.**

Наслідки: недоступний `dynamic_cast` (використовуй `static_cast`, коли тип відомий) і `typeid` (заміни на template specialization / tag dispatch). Virtual-функції працюють – vtable ≠ RTTI.

Правило: без RTTI покладайся на compile-time знання типів, а не runtime-перевірки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
