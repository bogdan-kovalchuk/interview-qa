---
id: emb-volconst-0040
title: "Що таке top-level і low-level `const` у pointer type?"
description: "Top-level const кваліфікує сам об'єкт pointer, low-level const кваліфікує pointed-to data."
track: embedded
section: volatile-and-const
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

**Top-level `const` кваліфікує сам об'єкт pointer, low-level `const` кваліфікує pointed-to data.**

У `int * const p` top-level const: `p` не можна переназначити. У `const int *p` low-level const: через `p` не можна змінити `*p`. Для API важливіше low-level const, бо воно описує, що функція робить із даними caller-а.

Правило: `const` після `*` захищає pointer; `const` перед base type захищає дані.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
