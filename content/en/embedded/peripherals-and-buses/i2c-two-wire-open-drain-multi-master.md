---
id: emb-periph-0007
title: "What is I2C?"
description: "I2C is a synchronous bus on two open-drain lines with pull-ups, supporting multi-master and 7-bit slave addressing."
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

**Inter-Integrated Circuit** – a synchronous serial interface.[^dou-embedded-interview] Only two wires: `SCL` (clock) and `SDA` (data), both open-drain + pull-up resistors.

Key point: devices on the bus can only **pull the line low**; the HIGH level is produced by the pull-up resistor. This lets multiple devices share one bus safely.

Multi-master, multi-slave; Each slave has a unique 7-bit address; Half-duplex; Speeds: 100 kHz, 400 kHz, 1 MHz; ACK/NACK supported; Typical: sensors, EEPROM, RTC, OLED.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
