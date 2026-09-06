---
id: emb-volconst-0009
title: "Що означає декларація `volatile uint32_t *p`?"
description: "p є вказівником на volatile uint32_t."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

**`p` є вказівником на volatile `uint32_t`**.

Сам вказівник `p` можна змінювати: він може вказувати на іншу адресу. Але кожне `*p` повинно бути реальним volatile-доступом до об'єкта. Це нормальна форма для доступу до hardware register, якщо адреса може вибиратися runtime.

Правило читання: починай від імені `p`: `p` is pointer to volatile `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
