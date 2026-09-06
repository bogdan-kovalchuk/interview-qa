---
id: emb-patterns-0011
title: "Trap: чому поле `count` у ring buffer створює race condition?"
description: "ISR (interrupt service routine) інкрементує count, main декрементує – це read-modify-write над спільною змінною."
track: embedded
section: common-code-patterns
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

ISR (interrupt service routine) інкрементує `count`, main декрементує – це read-modify-write над спільною змінною.

`count++` не атомарне (read, modify, write); якщо ISR переб'є main між цими кроками, оновлення загубиться -> off-by-one і пошкоджений стан буфера.

Захист: або критична секція/atomic, або взагалі без `count` – визначай full/empty лише з `head`/`tail`.[^embeddedinterviewlab]

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
