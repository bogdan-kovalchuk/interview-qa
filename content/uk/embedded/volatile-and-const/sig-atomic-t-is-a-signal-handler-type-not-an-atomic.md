---
id: emb-volconst-0044
title: "Trap: чи гарантує `volatile sig_atomic_t` ті самі властивості, що hardware atomic?"
description: "Ні. Це спеціальний portable C-патерн для signal handlers, а не загальний embedded atomic primitive."
track: embedded
section: volatile-and-const
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

Ні. Це спеціальний portable C-патерн для signal handlers, а не загальний embedded atomic primitive.

`sig_atomic_t` гарантує безпечний доступ у контексті C signal handler у межах стандартної бібліотеки, але це не означає, що будь-який volatile тип на MCU є атомарним або має memory ordering. Для ISR на bare-metal треба дивитися ширину bus, інструкції CPU і ABI.

Захист: для Cortex-M shared ISR data використовуй типи, які атомарно читаються/пишуться на цій архітектурі, або critical sections.[^embeddedinterviewlab]

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
