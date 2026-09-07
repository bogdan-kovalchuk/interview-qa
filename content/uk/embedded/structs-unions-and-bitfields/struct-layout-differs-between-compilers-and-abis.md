---
id: emb-structs-0053
title: "Trap: чи можна порівнювати layout C struct між різними компіляторами без перевірки?"
description: "Ні: ABI, alignment, packing pragmas і bit-field rules можуть відрізнятися."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Ні: ABI, alignment, packing pragmas і bit-field rules можуть відрізнятися.</span>

Навіть однаковий source може мати інші offsets або розмір на іншій архітектурі. Для host tool + MCU firmware це частий баг: PC tool пише binary file за своїм struct layout, firmware читає за іншим.

Захист: external binary formats описуй у байтах, не в C structs. Додай version, length, endian і static/runtime checks.[^embeddedinterviewlab]

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
