---
id: emb-rtos-0010
title: "Що таке RTOS і чим вона відрізняється від general-purpose OS за latency, scheduling і determinism?"
description: "<span class=\"key\">RTOS</span> дає bounded interrupt/task latency, priority-based scheduling і primitives для deterministic embedded tasks."
track: embedded
section: rtos
level: middle
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
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

<span class="key">RTOS</span> дає bounded interrupt/task latency, priority-based scheduling і primitives для deterministic embedded tasks. General-purpose OS оптимізує throughput, fairness і багатокористувацькі можливості, тому latency може бути менш передбачуваною. RTOS не гарантує «швидко завжди»; вона дає контрольовані worst-case умови, якщо код і пріоритети спроєктовані правильно.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

