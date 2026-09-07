---
id: emb-periph-0002
title: "Що таке `GPIO`?"
description: "GPIO – універсальний цифровий пін МК, що конфігурується на вхід, push-pull чи open-drain вихід або альтернативну функцію через регістри."
track: embedded
section: peripherals-and-buses
level: junior
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**General Purpose Input/Output** – універсальний цифровий пін мікроконтролера, що конфігурується програмно.

Режими: `Input` (з pull-up / pull-down / floating); `Output Push-Pull` – керує HIGH/LOW; `Output Open-Drain` – керує лише LOW, HIGH через зовнішній резистор; `Alternate Function` – пін підключається до UART/SPI/I2C/Timer.

Управління через регістри: `MODER`, `ODR`, `IDR`, `BSRR` (STM32). Атомарний запис: `BSRR` встановлює або скидає біт за один цикл без ризику race condition.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
