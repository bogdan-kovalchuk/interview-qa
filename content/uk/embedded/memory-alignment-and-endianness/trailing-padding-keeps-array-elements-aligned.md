---
id: emb-align-0006
title: "Навіщо структурі trailing (хвостовий) padding?"
description: "Щоб у масиві структур кожен наступний елемент теж був вирівняний."
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

**Щоб у масиві структур кожен наступний елемент теж був вирівняний.**

Якщо `sizeof(struct)` не кратний alignment найбільшого поля, то `arr[1]` почнеться за невирівняною адресою і доступ до його полів був би misaligned. Тому компілятор доповнює розмір до кратного.

Правило: саме через trailing padding `sizeof` структури – не сума полів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
