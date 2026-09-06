---
id: emb-fnptr-0027
title: "Trap: що небезпечно у виклику `printf` з ISR callback-а?"
description: "printf зазвичай не є ISR-safe і може бути blocking/reentrant-unsafe."
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

`printf` зазвичай не є ISR-safe і може бути blocking/reentrant-unsafe.

Воно може брати lock, використовувати heap, чекати UART TX або змінювати global state. В interrupt context це може спричинити deadlock, jitter або corrupt output, особливо якщо main code теж друкує.

Захист: у ISR callback став flag, записуй у lock-free/ring buffer або використовуй спеціальний non-blocking trace backend.[^embeddedinterviewlab]

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
