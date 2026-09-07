---
id: emb-fnptr-0045
title: "Trap: чому function pointer state machine може бути складнішою для аналізу?"
description: "Indirect calls приховують control flow від читача, debugger-а і деяких static analyzers."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Indirect calls приховують control flow від читача, debugger-а і деяких static analyzers.</span>

Замість явного `switch` видно лише `handlers[state](...)`. Якщо table ініціалізується runtime або змінюється, важче довести, які функції можуть викликатися. Це може вплинути на safety certification і MISRA-перевірки.

Захист: роби таблиці `static const`, іменуй handlers явно, перевіряй state bounds і документуй transition table.[^embeddedinterviewlab]

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
