---
id: emb-volconst-0010
title: "Що означає декларація `uint32_t * volatile p`?"
description: "p є volatile-вказівником на звичайний uint32_t."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

**`p` є volatile-вказівником на звичайний `uint32_t`**.

Тут volatile стосується самого значення pointer variable, а не даних за адресою. Компілятор має перечитувати адресу, що зберігається у `p`, але доступ `*p` не є volatile-доступом до hardware data.

Embedded-висновок: для регістрів майже завжди потрібен `volatile uint32_t *p`, а не `uint32_t * volatile p`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
