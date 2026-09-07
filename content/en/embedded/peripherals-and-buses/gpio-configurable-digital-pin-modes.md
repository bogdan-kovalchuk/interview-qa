---
id: emb-periph-0002
title: "What is `GPIO`?"
description: "GPIO is a software-configurable digital MCU pin supporting input, push-pull, open-drain, and alternate function modes."
track: embedded
section: peripherals-and-buses
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
    applicability: "Authoritative section-level reference for peripherals and buses concepts; details of specific devices and toolchains can differ."
---

## Short answer

**General Purpose Input/Output** – a general-purpose digital microcontroller pin configured in software.

Modes: `Input` (with pull-up / pull-down / floating); `Output Push-Pull` – drives HIGH/LOW; `Output Open-Drain` – drives only LOW, HIGH via an external resistor; `Alternate Function` – the pin is routed to UART/SPI/I2C/Timer.

Control via registers: `MODER`, `ODR`, `IDR`, `BSRR` (STM32). Atomic write: `BSRR` sets or clears a bit in one cycle with no race-condition risk.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
