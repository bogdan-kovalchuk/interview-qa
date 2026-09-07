---
id: emb-patterns-0038
title: "Чому function-pointer FSM table роблять `static const`?"
description: "static const кладе таблицю у Flash/.rodata – економить RAM і захищає mapping від випадкового перезапису в runtime."
track: embedded
section: common-code-patterns
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

**`static const` кладе таблицю у Flash/`.rodata`** – економить RAM і захищає mapping від випадкового перезапису в runtime.

Якщо переходи FSM (finite state machine) не змінюються після збірки, mutable global масив – зайвий ризик (corruption перенаправить виклик у випадкову адресу).

Правило: незмінні dispatch/handler таблиці – завжди `static const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
