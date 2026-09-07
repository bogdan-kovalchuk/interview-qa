---
id: emb-hwbasic-0002
title: "What kinds of microcontrollers have you worked with?"
description: "Common MCU families for interviews are ARM Cortex-M (STM32), AVR (ATmega328), ESP32 and RP2040, each with its own niche and peripherals."
track: embedded
section: hardware-basics
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for hardware basics concepts; details of specific devices and toolchains can differ."
---

## Short answer

The answer is individual, but it is worth mentioning MCU families and their features:[^dou-embedded-interview]

- **ARM Cortex-M**: STM32 (F1/F4/H7) – most common in industry; HAL and LL libraries, CubeMX.
- **AVR**: ATmega328 (Arduino Uno) – 8-bit, easy start, well documented.
- **ESP32**: Wi-Fi/BT, dual-core Xtensa LX6, FreeRTOS – IoT applications.
- **RP2040**: dual-core ARM M0+, PIO for flexible peripheral I/O.

At an interview: name the MCU, describe which peripheral block you configured (UART/SPI/DMA/PWM) and for what task.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
