---
id: emb-volconst-0030
title: "Trap: що небезпечно в `char *p = \"OK\"; p[0] = 'N';`?"
description: "Запис у string literal має undefined behavior."
track: embedded
section: volatile-and-const
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

<span class="warn">Запис у string literal має undefined behavior.</span>

У C string literal часто лежить у read-only області, наприклад `.rodata` у Flash. Історично C дозволяє присвоїти literal у `char *` з попередженням у деяких компіляторах, але модифікація об'єкта за цим pointer заборонена семантично і може дати HardFault на MCU.

Захист: використовуй `const char *p = "OK";` або mutable array: `char p[] = "OK";`.[^embeddedinterviewlab]

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
