---
id: emb-structs-0028
title: "Trap: чи portable порядок bit-field-ів у пам'яті?"
description: "Ні: порядок allocation bit-field-ів у storage unit implementation-defined."
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

<span class="warn">Ні: порядок allocation bit-field-ів у storage unit implementation-defined.</span>

Один компілятор може розміщувати перше поле в least significant bits, інший або інший ABI може поводитися інакше. Endianness також не дає простого portable правила для bit-field layout у bytes.

Захист: не використовуй bit-fields як wire format між різними compiler/targets. Для protocol bits використовуй masks/shifts над integer, отриманим із явно розпарсених bytes.[^embeddedinterviewlab]

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
