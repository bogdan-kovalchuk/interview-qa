---
id: emb-dtypes-0105
title: "Чим DRAM відрізняється від SRAM і які наслідки це має для latency, refresh, controller і startup?"
description: "SRAM швидка, проста для MCU, не потребує refresh, але дорога за площу. DRAM щільніша і більша, але потребує memory controller, refresh, calibration/training і має складнішу latency."
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

**SRAM** швидка, проста для MCU, не потребує refresh, але дорога за площу і зазвичай менша. **DRAM** щільніша і більша, але потребує memory controller, refresh, calibration/training і має складнішу latency. На startup DRAM може бути недоступна до ініціалізації controller, тому early boot часто працює з internal SRAM.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
