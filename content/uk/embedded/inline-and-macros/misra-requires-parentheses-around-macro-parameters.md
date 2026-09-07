---
id: emb-macros-0020
title: "Що вимагає MISRA C Rule 20.7 і навіщо?"
description: "MISRA C (Motor Industry Software Reliability Association C) Rule 20.7 вимагає брати в дужки macro parameters, які беруть участь у виразах, щоб уникнути помилок operator precedence після розгортання."
track: embedded
section: inline-and-macros
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**MISRA C (Motor Industry Software Reliability Association C) Rule 20.7 вимагає брати в дужки macro parameters, які беруть участь у виразах**, щоб уникнути помилок operator precedence після розгортання.

Тобто `#define ADD(a,b) a+b` небезпечний; коректно `#define ADD(a,b) ((a) + (b))`. Це прибирає баги типу `ADD(1,2) * 3`, де без дужок було б `1 + 2 * 3`.

Правило: 20.7 не робить макроси бажаними; разом із Rule 4.9 воно підштовхує замінювати function-like макроси на `static inline`, коли це можливо.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
