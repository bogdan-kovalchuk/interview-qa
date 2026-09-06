---
id: emb-structs-0041
title: "Trap: як padding може стати витоком інформації?"
description: "Якщо відправити або записати raw bytes структури, padding може містити старі дані зі stack/RAM."
track: embedded
section: structs-unions-and-bitfields
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

Якщо відправити або записати raw bytes структури, padding може містити старі дані зі stack/RAM.

Наприклад, `send(fd, &msg, sizeof msg)` може включити padding bytes між полями. Ці bytes не ініціалізуються окремим assignment до полів і можуть містити фрагменти попередніх змінних.

Захист: zero-initialize структуру перед заповненням, серіалізуй поля явно і не експортуй raw struct layout як security boundary.[^embeddedinterviewlab]

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
