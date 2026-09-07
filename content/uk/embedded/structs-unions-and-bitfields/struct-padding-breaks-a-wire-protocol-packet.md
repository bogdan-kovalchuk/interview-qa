---
id: emb-structs-0006
title: "Trap: чому не можна напряму відправляти `sizeof(struct)` байтів як protocol packet?"
description: "Бо структура може містити padding bytes і ABI-залежний layout."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Бо структура може містити padding bytes і ABI-залежний layout.</span>

Padding bytes можуть мати невизначені значення, порядок байтів залежить від endianness, а offsets можуть відрізнятися між компіляторами, опціями packing і target ABI. Те, що працює між двома однаковими Cortex-M build-ами, може зламатися при зміні compiler або protocol peer.

Захист: серіалізуй поля явно у buffer, задавай endian формат і перевіряй довжину packet. Для fixed binary layout використовуй static assertions і controlled packing.[^embeddedinterviewlab]

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
