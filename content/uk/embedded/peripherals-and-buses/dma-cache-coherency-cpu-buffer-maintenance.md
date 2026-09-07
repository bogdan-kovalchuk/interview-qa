---
id: emb-periph-0010
title: "Що таке DMA і які проблеми виникають між DMA, cache і CPU?"
description: "<span class=\"key\">DMA</span> переносить дані між peripheral і memory без копіювання кожного байта CPU."
track: embedded
section: peripherals-and-buses
level: middle
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**DMA** переносить дані між peripheral і memory без копіювання кожного байта CPU. Проблема в тому, що CPU cache може містити старі або ще не записані дані, а DMA бачить RAM напряму. Перед TX потрібен clean/flush cache, після RX – invalidate, плюс правильне alignment, memory barriers і buffers у DMA-accessible memory.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

