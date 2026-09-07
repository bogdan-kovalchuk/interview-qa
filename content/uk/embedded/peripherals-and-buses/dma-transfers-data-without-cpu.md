---
id: emb-periph-0006
title: "Що таке DMA?"
description: "DMA передає дані між периферією і пам'яттю без постійної участі CPU, знижуючи навантаження й стабілізуючи timing."
track: embedded
section: peripherals-and-buses
level: junior
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

**DMA (Direct Memory Access)** – механізм передачі даних між периферією і пам'яттю або між ділянками пам'яті без постійної участі CPU.[^dou-embedded-interview]

Приклад: UART RX або ADC пише дані прямо в RAM buffer, а CPU лише налаштовує DMA controller: адресу периферії, адресу буфера, розмір, напрямок і режим. Після завершення DMA може згенерувати interrupt.

Переваги: менше навантаження CPU, вища швидкість, стабільніший timing. Типові задачі: SPI/UART/I2C transfers, ADC sampling, audio buffers, display refresh.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
