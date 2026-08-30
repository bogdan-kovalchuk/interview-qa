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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? peripherals-and-buses; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">General Purpose Input/Output</span> – універсальний цифровий пін мікроконтролера, що конфігурується програмно.<br><br>Режими: <code>Input</code> (з pull-up / pull-down / floating); <code>Output Push-Pull</code> – керує HIGH/LOW; <code>Output Open-Drain</code> – керує лише LOW, HIGH через зовнішній резистор; <code>Alternate Function</code> – пін підключається до UART/SPI/I2C/Timer.<br><br>Управління через регістри: <code>MODER</code>, <code>ODR</code>, <code>IDR</code>, <code>BSRR</code> (STM32). Атомарний запис: <code>BSRR</code> встановлює або скидає біт за один цикл без ризику race condition.[^dou-embedded-interview]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
