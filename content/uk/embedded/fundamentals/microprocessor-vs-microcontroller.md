---
id: emb-fund-0008
title: "В чому полягає різниця між мікропроцесором і мікроконтролером?"
description: "Мікропроцесор (MPU) – це переважно CPU, що потребує зовнішньої пам'яті й периферії для ОС, а мікроконтролер (MCU) інтегрує CPU, Flash, RAM і периферію на одному кристалі."
track: embedded
section: fundamentals
level: junior
type: comparison
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

**Мікропроцесор (MPU)** – переважно CPU, що зазвичай потребує зовнішньої RAM, Flash і периферії.[^dou-embedded-interview] Висока продуктивність, частіше запускає повноцінну ОС; приклади: Intel Core, ARM Cortex-A.

**Мікроконтролер (MCU)** – CPU + Flash + RAM + GPIO/UART/SPI/ADC/таймери на одному кристалі. Низьке споживання, дешевший, детермінована поведінка; багато MCU, наприклад ARM Cortex-M, використовують **modified Harvard architecture**, але не всі MCU треба категорично називати Harvard.

Вибір: MPU – ОС і складні обчислення; MCU – управління апаратурою в реальному часі.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
