---
id: emb-dtypes-0103
title: "Що таке hardware registers і чим memory-mapped register відрізняється від CPU general-purpose register?"
description: "Hardware register керує peripheral або відображає його status.Memory-mapped register доступний як адреса у memory map і зазвичай оголошується через vo…"
track: embedded
section: data-types-and-memory-layout
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Hardware register** керує peripheral або відображає його status. **Memory-mapped register** доступний як адреса у memory map і зазвичай оголошується через `volatile` pointer/struct. CPU general-purpose register - внутрішній register ядра для обчислень; він не є peripheral control register.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
