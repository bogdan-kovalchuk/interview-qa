---
id: emb-structs-0014
title: "Що таке `union` у C?"
description: "union зберігає кілька альтернативних полів в одній і тій самій області пам'яті; розмір union дорівнює розміру найбільшого member-а з урахуванням alignment."
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

**`union`** зберігає кілька альтернативних полів в одній і тій самій області пам'яті; розмір union дорівнює розміру найбільшого member-а з урахуванням alignment.

На відміну від struct, поля union не лежать послідовно. Усі member-и починаються з offset 0 і перекриваються. Запис в один member змінює bytes, які будуть видимі через інші member-и.

Embedded-use cases: variant data, register views, protocol payload alternatives, raw byte access з обережністю щодо aliasing і endianness.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
