---
id: emb-volconst-0024
title: "Чому `const` важливий для embedded не лише як захист від запису?"
description: "const дозволяє розмістити file-scope/static read-only дані у Flash, зазвичай у .rodata."
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

**`const` дозволяє розмістити file-scope/static read-only дані у Flash, зазвичай у `.rodata`**.

Без `const` ініціалізований глобальний масив потрапить у `.data`: початкові байти зберігаються у Flash, але при старті копіюються в RAM. На MCU з 16 KB RAM lookup table на 1 KB може бути відчутною втратою.

Правило: calibration tables, strings, protocol descriptors, CRC tables і LUT, які не змінюються, оголошуй як `const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
