---
id: emb-memlink-0013
title: "Що таке heap fragmentation і як вона проявляється у long-running firmware?"
description: "Типова помилка в embedded-коді та її наслідки."
track: embedded
section: memory-and-linker
level: middle
type: pitfall
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Heap fragmentation** – ситуація, коли вільної пам'яті сумарно вистачає, але вона розбита на малі несуміжні блоки. У firmware це проявляється як випадкові `malloc` failures після годин або днів роботи, особливо при різних розмірах allocation. Типова профілактика: fixed-size pools, allocate-on-startup, bounded lifetimes і відсутність heap у ISR.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
