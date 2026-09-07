---
id: emb-fnptr-0051
title: "Trap: чому callback може бути reentrancy problem?"
description: "Callback може бути викликаний повторно до завершення попереднього виклику."
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

<span class="warn">Callback може бути викликаний повторно до завершення попереднього виклику.</span>

Наприклад, UART RX interrupt може прийти під час обробки попереднього байта, або callback може викликати API, який синхронно породжує новий callback. Якщо callback використовує static local buffer без захисту, стан може пошкодитися.

Захист: документуй reentrancy, мінімізуй shared mutable state, використовуй queues/critical sections або забороняй nested callbacks design-ом.[^embeddedinterviewlab]

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
