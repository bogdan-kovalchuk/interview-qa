---
id: emb-volconst-0056
title: "Що означає `static const` для таблиці всередині C-файлу?"
description: "static обмежує linkage цим translation unit, а const робить дані read-only через цей identifier."
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

**`static` обмежує linkage цим translation unit, а `const` робить дані read-only через цей identifier.**

Для embedded lookup table це часто ідеальна форма: символ не експортується назовні, дані можуть лежати у `.rodata`/Flash, а compiler може оптимізувати доступи в межах файлу.

Правило: file-private immutable tables оголошуй як `static const`, якщо вони не мають бути частиною зовнішнього ABI.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
