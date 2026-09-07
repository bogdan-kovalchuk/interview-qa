---
id: emb-conn-0012
title: "Що стоїть між network interface і MCU: PHY, MAC, transceiver, controller, DMA і driver stack?"
description: "Physical medium обслуговує PHY/transceiver, MAC/controller формує frames, filters, interrupts і працює з DMA descriptors, driver stack ініціалізує hardware, керує buffers/cache coherency, обробляє IRQ."
track: embedded
section: connectivity
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
    applicability: "Авторитетне джерело рівня секції для понять розділу connectivity; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Physical medium обслуговує **PHY/transceiver**, який перетворює electrical/radio signals у digital link signals. **MAC/controller** формує frames, filters, interrupts і часто працює з DMA descriptors у RAM. Driver stack ініціалізує hardware, керує buffers/cache coherency, обробляє IRQ і передає packets у TCP/IP або fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
