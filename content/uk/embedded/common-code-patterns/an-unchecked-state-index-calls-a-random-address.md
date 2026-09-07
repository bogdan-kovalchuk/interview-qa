---
id: emb-patterns-0040
title: "Trap: що буде, якщо в state machine не перевірити індекс стану перед `handlers[state]`?"
description: "Невалідний/пошкоджений стан -> out-of-bounds read таблиці й indirect call за випадковою адресою (ймовірний HardFault)."
track: embedded
section: common-code-patterns
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

<span class="warn">Невалідний/пошкоджений стан -> out-of-bounds read таблиці й indirect call за випадковою адресою</span> (ймовірний HardFault).

Дані стають control flow, тож стан із зовнішнього входу чи corruption напряму керує тим, яку функцію викличуть.

Захист: `if (state < ARRAY_SIZE(handlers) && handlers[state]) handlers[state](evt); else on_error();`[^embeddedinterviewlab]

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
