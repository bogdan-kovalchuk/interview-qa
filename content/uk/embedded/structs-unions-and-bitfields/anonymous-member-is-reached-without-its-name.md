---
id: emb-structs-0044
title: "Що таке anonymous struct/union і де це зустрічається?"
description: "Anonymous struct/union дозволяє звертатися до вкладених member-ів без імені проміжного об'єкта, якщо це підтримується стандартом/компілятором у відповідному режимі."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Anonymous struct/union** дозволяє звертатися до вкладених member-ів без імені проміжного об'єкта, якщо це підтримується стандартом/компілятором у відповідному режимі.

У embedded headers це часто використовують для register views: один register можна бачити як raw `uint32_t` або як набір fields. Це зручно, але може бути compiler-specific у старих C режимах.

Правило: перевіряй, чи anonymous union/struct дозволені стандартом і coding standard проекту; для portable public headers краще бути обережним.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
