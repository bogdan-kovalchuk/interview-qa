---
id: emb-volconst-0033
title: "Коли cast-away `const` не є UB, а коли стає UB?"
description: "Cast-away const сам по собі не обов'язково UB; UB виникає при записі в об'єкт, який реально був оголошений const."
track: embedded
section: volatile-and-const
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

**Cast-away `const` сам по собі не обов'язково UB; UB виникає при записі в об'єкт, який реально був оголошений `const`.**

Якщо є mutable object `uint32_t x`, потім `const uint32_t *cp = &x`, то технічно можна повернути `uint32_t *p = (uint32_t *)cp` і змінити `x`. Але це поганий API-сигнал. Якщо object був `const uint32_t cfg`, запис через cast має undefined behavior.

Правило: не використовуй cast для обходу type contract; виправляй сигнатуру або ownership моделі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
