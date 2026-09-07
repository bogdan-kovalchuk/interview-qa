---
id: emb-fund-0025
title: "Як вибрати між MCU, DSP, FPGA або аналоговим контролером для задачі керування силовою частиною?"
description: "MCU підходить для control logic, communication і помірних loops; DSP - для швидких чисельних control algorithms. FPGA дає паралельність і deterministic sub-microsecond timing. Аналоговий контролер доречний для простої, дуже швидкої або fail-safe regulation."
track: embedded
section: fundamentals
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**MCU** підходить для control logic, communication і помірних loops; **DSP** - для швидких чисельних control algorithms. **FPGA** дає паралельність і deterministic sub-microsecond timing, але дорожча у розробці. Аналоговий контролер доречний, коли потрібна проста, дуже швидка або fail-safe regulation без залежності від firmware.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
