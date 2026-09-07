---
id: emb-testemb-0002
title: "Як тестувати embedded C-код на host і на target, і що саме має покривати кожен рівень?"
description: "Host tests покривають чисту логіку: state machines, parsers, protocol framing, boundary cases, mocks для HAL/MMIO.Target tests перевіряють те, що зале…"
track: embedded
section: testing-embedded
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
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу testing-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Host tests** покривають чисту логіку: state machines, parsers, protocol framing, boundary cases, mocks для HAL/MMIO. **Target tests** перевіряють те, що залежить від заліза: clocks, drivers, DMA, ISR latency, buses, power states і real timing. HIL або board tests мають ловити інтеграційні дефекти, які unit tests на PC не бачать.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

