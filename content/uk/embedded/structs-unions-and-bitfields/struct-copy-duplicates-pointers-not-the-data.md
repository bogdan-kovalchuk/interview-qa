---
id: emb-structs-0051
title: "Trap: чому копіювання struct із pointer fields може бути shallow copy багом?"
description: "Structure assignment копіює pointer value, а не дані, на які він вказує."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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

Structure assignment копіює pointer value, а не дані, на які він вказує.

Після `b = a` обидві структури можуть вказувати на той самий buffer. Якщо одна структура звільняє або змінює buffer, інша бачить наслідки. У embedded це часто трапляється з DMA buffers, queues і driver config pointers.

Захист: визнач ownership: або pointer є borrowed і це документовано, або потрібна deep copy, або buffer передається окремо з lifetime contract.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
