---
id: emb-macros-0019
title: "Що вимагає MISRA C Rule 4.9 щодо function-like макросів?"
description: "MISRA C (Motor Industry Software Reliability Association C) вимагає надавати перевагу функціям, а не function-like макросам, де вони взаємозамінні."
track: embedded
section: inline-and-macros
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

**MISRA C (Motor Industry Software Reliability Association C) вимагає надавати перевагу функціям, а не function-like макросам**, де вони взаємозамінні.

Обґрунтування: макроси обходять type checking, можуть обчислювати аргументи непередбачувано (double evaluation) і ускладнюють дебаг та статичний аналіз.

Практичний наслідок: у safety-critical проєктах заміняй function-like макроси на `static inline`; макроси лишай для того, що функцією бути не може (register defs, conditional compilation, X-macros).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
