---
id: emb-fnptr-0043
title: "Trap: що не так із реєстрацією callback-а без unregister?"
description: "Driver може викликати callback після знищення module/object-а."
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

Driver може викликати callback після знищення module/object-а.

Особливо у C++ embedded: object destructor може завершитися, але C HAL усе ще зберігає `ctx = this`. Наступний interrupt викликає thunk із dangling `this` pointer.

Захист: у destructor або shutdown path unregister callback і disable interrupts/events перед знищенням state. Визнач ownership у API.[^embeddedinterviewlab]

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
