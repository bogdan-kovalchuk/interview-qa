---
id: emb-align-0034
title: "Trap: чому розкладка bitfield-ів непортативна між платформами?"
description: "Стандарт не визначає ані порядок бітів усередині слова, ані storage unit – це implementation-defined."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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

<span class="warn">Стандарт не визначає ані порядок бітів усередині слова, ані storage unit – це implementation-defined.</span>

На LE і BE (та між різними компіляторами) поля можуть пакуватися з протилежних кінців, тож той самий bitfield-struct дасть різні біти на дроті.

Захист: для протоколів/регістрів не покладайся на bitfields у wire-форматі; використовуй явні маски та зсуви над `uint32_t`.[^embeddedinterviewlab]

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
