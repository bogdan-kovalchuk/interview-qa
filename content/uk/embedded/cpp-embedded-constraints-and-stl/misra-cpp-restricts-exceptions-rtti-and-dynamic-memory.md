---
id: emb-cppstl-0023
title: "Що зазвичай обмежують MISRA C++ правила в embedded C++?"
description: "MISRA (Motor Industry Software Reliability Association) C++ обмежує exception-based control flow, dynamic allocation, RTTI (run-time type information), небезпечні casts, goto, складну inheritance-ієрархію та сирі unions."
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

**MISRA (Motor Industry Software Reliability Association) C++ обмежує exception-based control flow, dynamic allocation, RTTI (run-time type information), небезпечні casts, `goto`, складну inheritance-ієрархію та сирі unions.**

Мета – детермінізм, аналізованість і контрольований data/control flow. Конкретні формулювання залежать від версії стандарту й профілю проєкту, тому на співбесіді краще казати «обмежує/регламентує», а не «забороняє все».

Правило: MISRA C++ – про передбачуваність; під неї пишуть із return codes, static allocation і мінімумом runtime-магії.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
