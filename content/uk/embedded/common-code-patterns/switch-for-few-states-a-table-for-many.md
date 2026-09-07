---
id: emb-patterns-0029
title: "Коли обирати enum+switch, а коли function-pointer table для FSM?"
description: "enum+switch – мало станів (<~8), важлива простота дебагу і warning на пропущені case."
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

**enum+switch** – мало станів (<~8), важлива простота дебагу і warning на пропущені case.

Function-pointer table – багато станів, потрібна O(1) диспетчеризація і додавання станів без зміни наявного коду (таблиця у Flash).

Правило: малий FSM (finite state machine) – switch; великий/динамічний – таблиця handler-ів з bounds-check і default.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
