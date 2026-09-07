---
id: emb-raii-0006
title: "Як виглядає interrupt-disable RAII guard і чому він безпечний у ISR?"
description: "Ctor зберігає поточний стан переривань і вимикає їх; dtor відновлює попередній стан."
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

**Ctor зберігає поточний стан переривань і вимикає їх; dtor відновлює попередній стан.**

ISR означає interrupt service routine. Guard оперує лише регістром PRIMASK (interrupt mask register), без блокуючих викликів, тож може бути допустимим навіть у ISR-контексті. Відновлення попереднього стану (а не безумовний enable) дозволяє вкладеність.

Правило: найбезпечніший RAII в ISR – register-level interrupt disable/restore; не використовуй там мьютекси чи heap.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
