---
id: emb-fnptr-0057
title: "Trap: чому indirect call через function pointer може бути проблемою в safety-critical firmware?"
description: "Він переносить control-flow decision у дані."
track: embedded
section: function-pointers-and-callbacks
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

Він переносить control-flow decision у дані.

Якщо function pointer перезаписаний через memory corruption, out-of-bounds або stack bug, програма може перейти в непередбачуваний код. Для safety/security це серйозний ризик, особливо якщо таблиці mutable в RAM.

Захист: роби dispatch tables `const` у Flash, перевіряй індекси, не приймай function addresses із зовнішнього input, увімкни MPU/stack protection там, де доступно.[^embeddedinterviewlab]

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
