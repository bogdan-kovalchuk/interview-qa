---
id: emb-fnptr-0018
title: "Що таке dispatch table на function pointers?"
description: "Dispatch table – це масив function pointer-ів, де індекс або opcode вибирає функцію для виклику."
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

**Dispatch table** – це масив function pointer-ів, де індекс або opcode вибирає функцію для виклику.

Наприклад, command parser може мати `cmd_handler_t table[256]`, де `table[opcode](ctx, frame)` обробляє команду. Це прибирає великий `switch`, але потребує перевірки індексу і default handler-а.

Embedded-use case: CLI commands, protocol opcodes, state machine actions, test command handlers.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
