---
id: emb-structs-0039
title: "Чим відрізняються assignment і `memcpy` для структур?"
description: "Structure assignment копіює значення структури як цілий object; practically це може включати padding bytes, але semantics описує копіювання member values."
track: embedded
section: structs-unions-and-bitfields
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

**Structure assignment копіює значення структури як цілий object**; practically це може включати padding bytes, але semantics описує копіювання member values.

`memcpy` копіює raw object representation byte-by-byte. Для trivially stored C structs обидва часто дають однаковий observable результат для полів, але `memcpy` може скопіювати padding із невизначеними байтами.

Правило: для звичайного копіювання structs використовуй assignment; для wire/storage serialization не копіюй padding bytes без потреби.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
