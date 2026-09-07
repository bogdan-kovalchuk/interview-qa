---
id: emb-volconst-0017
title: "Що означає `uint8_t * const buf` у параметрі або локальній змінній?"
description: "buf є const pointer to mutable uint8_t."
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

**`buf` є const pointer to mutable `uint8_t`**.

Не можна присвоїти `buf = other`, але можна змінювати `buf[0]`. У параметрі функції top-level `const` на самому pointer рідко є частиною API, бо параметр і так копія pointer value.

Embedded-use case: локальний alias на фіксовану адресу або register pointer, який не має бути випадково переназначений.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
