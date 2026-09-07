---
id: emb-fnptr-0021
title: "Чому dispatch table може бути кращою за великий `switch`?"
description: "Вона відокремлює mapping opcode -> handler від логіки handler-ів і спрощує додавання команд."
track: embedded
section: function-pointers-and-callbacks
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

**Вона відокремлює mapping opcode -> handler від логіки handler-ів** і спрощує додавання команд.

У embedded protocol parser це може зменшити cyclomatic complexity і дозволити зберігати таблицю у Flash як `static const`. Але indirect calls можуть бути менш прозорими для optimizer-а і складнішими для static analysis.

Правило: dispatch table добра для стабільних opcode maps; для маленького switch із 3-5 cases простий `switch` часто читабельніший.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
