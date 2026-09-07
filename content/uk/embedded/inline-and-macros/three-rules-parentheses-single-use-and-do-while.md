---
id: emb-macros-0006
title: "Які три правила безпечного function-like макроса?"
description: "Дужки навколо кожного використання параметра, дужки навколо всього виразу і do { ... } while(0) для statement-макроса."
track: embedded
section: inline-and-macros
level: junior
type: concept
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

1. **Дужки навколо кожного використання параметра**: `(x)`;
2. **Дужки навколо всього виразу**: `((x) + (y))`;
3. **Statement-макрос обгортай у `do { ... } while(0)`**, щоб він коректно поводився з `if/else` і вимагав `;`.

Правило: ці три пункти прибирають більшість класичних macro-багів – precedence, обрізані вирази та зламаний control flow.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
