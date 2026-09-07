---
id: emb-cppstl-0024
title: "Чим AUTOSAR C++14 відрізняється від MISRA C++?"
description: "AUTOSAR (AUTomotive Open System ARchitecture) C++14 – автомобільний rule set для сучасного C++14; він регламентує templates, constexpr, auto, range-based for та інші фічі."
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

**AUTOSAR (AUTomotive Open System ARchitecture) C++14 – автомобільний rule set для сучасного C++14; він регламентує templates, `constexpr`, `auto`, range-based for та інші фічі.**

Це не «C++ заборонений», а набір правил для безпечного застосування мови в safety-critical коді. MISRA C++ і AUTOSAR близькі за метою, але мають різні видання, scope і конкретні правила.

Правило: AUTOSAR C++14 = сучасний C++ у межах safety-дисципліни, а не дозвіл писати будь-які abstraction без контролю.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
