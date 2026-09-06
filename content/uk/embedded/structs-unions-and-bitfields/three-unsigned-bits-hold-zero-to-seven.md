---
id: emb-structs-0021
title: "Яким буде діапазон `unsigned mode : 3`?"
description: "Від 0 до 7. Три unsigned bits представляють 2^3 = 8 значень."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

**Від `0` до `7`**.

Три unsigned bits представляють `2^3 = 8` значень. Запис значення поза діапазоном у unsigned bit-field зазвичай обрізається modulo `2^width`, але варто не покладатися на це як на validation logic.

Embedded-правило: перед записом у bit-field або register field маскуй і перевіряй значення явно, особливо якщо джерело з protocol/input.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
