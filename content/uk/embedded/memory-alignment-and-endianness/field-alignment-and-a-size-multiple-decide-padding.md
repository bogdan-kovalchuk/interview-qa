---
id: emb-align-0003
title: "Які два правила визначають padding у структурі?"
description: "1. Кожне поле лежить за адресою, кратною його natural alignment (між полями вставляється padding)."
track: embedded
section: memory-alignment-and-endianness
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

1. Кожне поле лежить за адресою, кратною його natural alignment (між полями вставляється padding). 2. Розмір усієї структури кратний alignment найбільшого поля (trailing padding) – щоб у масиві структур кожен елемент теж був вирівняний.

Правило: `sizeof(struct)` ≠ сума розмірів полів; завжди враховуй внутрішній і хвостовий padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
