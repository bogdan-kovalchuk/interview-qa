---
id: emb-structs-0034
title: "Trap: що не так із старим патерном `uint8_t data[1]` в кінці структури?"
description: "Це не flexible array member, а реальний масив з 1 байта."
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

Це не flexible array member, а реальний масив з 1 байта.

`sizeof(struct)` включає цей байт і padding після нього. Код, який виділяє `sizeof(struct) + len`, може отримати off-by-one layout або залежати від нестандартного extension. Сучасний C має стандартний синтаксис `data[]`.

Захист: для C99+ використовуй flexible array member `uint8_t data[];` і акуратно рахуй allocation size з overflow checks.[^embeddedinterviewlab]

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
