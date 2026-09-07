---
id: emb-raii-0030
title: "Який найбезпечніший RAII-патерн для використання в ISR?"
description: "Interrupt-disable/restore scope guard – лише register-level операції."
track: embedded
section: raii-and-smart-pointers
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

**Interrupt-disable/restore scope guard – лише register-level операції.**

Він зберігає PRIMASK (interrupt mask register), вимикає переривання в ctor і відновлює попередній стан у dtor. Жодних блокуючих чи heap-операцій, тому це один із небагатьох RAII-патернів, допустимих в interrupt context.

Правило: в ISR (interrupt service routine) RAII має чіпати тільки регістри; усе блокуюче – поза перериванням.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
