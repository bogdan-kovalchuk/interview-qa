---
id: emb-structs-0048
title: "Що таке common initial sequence у union зі struct-ами?"
description: "У C дозволено інспектувати common initial part структур у union за певних умов, коли структури мають сумісні початкові members."
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

**У C дозволено інспектувати common initial part структур у union за певних умов**, коли структури мають сумісні початкові members.

Цей патерн використовують для tagged variants, де перше поле – tag/type, спільне для всіх варіантів. Але це тонка частина стандарту, і її легко неправильно перенести в C++ або зламати зміною layout.

Правило: для простоти і переносимості часто краще винести tag поза union, ніж покладатися на common initial sequence.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
