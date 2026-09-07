---
id: emb-macros-0049
title: "Як `inline` впливає на code size у embedded?"
description: "Inline прибирає overhead виклику, але дублює тіло функції в кожному місці виклику."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 3
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

**Inline прибирає overhead виклику, але дублює тіло функції в кожному місці виклику.**

Для крихітних функцій це часто зменшує код (виклик дорожчий за тіло). Для більших або часто викликаних – навпаки <span class="warn">роздуває flash і тисне на I-cache</span>, інколи сповільнюючи систему.

Правило: `inline` дрібні хелпери; великі функції лишай звичайними і довіряй оптимізатору. На обмеженому flash зважуй `-Os` і реальний map-файл.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
