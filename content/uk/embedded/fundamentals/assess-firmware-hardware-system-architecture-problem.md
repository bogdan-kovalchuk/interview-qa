---
id: emb-fund-0028
title: "Як оцінити, чи має проблему вирішувати firmware, hardware design або system architecture?"
description: "Спочатку визнач симптом, constraint і failure mode. Firmware доречний для sequencing, filtering, diagnostics; hardware - для signal integrity, protection, analog limits. System architecture потрібна, коли проблема виникає з невірного розподілу відповідальності."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Спочатку визнач симптом, constraint і failure mode: timing, noise margin, resource limit, protocol mismatch чи requirement gap. Firmware доречний для sequencing, filtering, diagnostics і policy; hardware - для signal integrity, protection, analog limits і deterministic safety cutoff. **System architecture** потрібна, коли проблема виникає з невірного розподілу відповідальності між blocks або неможливих requirements.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
