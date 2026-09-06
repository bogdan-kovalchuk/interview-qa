---
id: emb-fnptr-0038
title: "Trap: чому capturing lambda не можна напряму передати як `void (*)(void)`?"
description: "Capturing lambda є object-ом зі станом, а не просто адресою функції."
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

Capturing lambda є object-ом зі станом, а не просто адресою функції.

Вона потребує storage для captured variables і викликається через `operator()`. C function pointer не має місця для state. Тому компілятор не може неявно перетворити capturing lambda на `void (*)(void)`.

Захист: передавай state через `void *ctx`, або використовуй C++ callback abstraction, якщо embedded constraints дозволяють.[^embeddedinterviewlab]

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
