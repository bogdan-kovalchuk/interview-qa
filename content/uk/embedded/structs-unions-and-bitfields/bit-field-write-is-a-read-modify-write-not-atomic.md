---
id: emb-structs-0049
title: "Trap: чи можна використовувати bit-field як atomic flag між ISR і main?"
description: "Не варто. Запис bit-field зазвичай є read-modify-write storage unit-а."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Не варто.</span>

Запис bit-field зазвичай є read-modify-write storage unit-а. Якщо ISR і main змінюють різні bit-fields в одному storage unit, один запис може перетерти інший. `volatile` не робить цю операцію атомарною.

Захист: для ISR flags використовуй окремі volatile byte/word flags, atomic masks з critical section або RTOS event flags.[^embeddedinterviewlab]

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
