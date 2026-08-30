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

<span class="key">DMA</span> переносить дані між peripheral і memory без копіювання кожного байта CPU. Проблема в тому, що CPU cache може містити старі або ще не записані дані, а DMA бачить RAM напряму. Перед TX потрібен clean/flush cache, після RX – invalidate, плюс правильне alignment, memory barriers і buffers у DMA-accessible memory.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

