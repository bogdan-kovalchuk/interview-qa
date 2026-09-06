---
id: emb-patterns-0033
title: "Чому варто визначати поля регістра через MASK+SHIFT, а не «магічні числа»?"
description: "Пари MASK+SHIFT самодокументовані й централізують layout регістра."
track: embedded
section: common-code-patterns
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Пари MASK+SHIFT самодокументовані й централізують layout регістра.**

`(reg & PRESC_MASK) >> PRESC_SHIFT` явно каже, яке поле читається; магічні `(reg & 0x70) >> 4` розкидані по коду легко розсинхронізувати з datasheet.

Правило: один `#define` MASK і один SHIFT на поле; використовуй їх і для читання, і для read-modify-write запису.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
