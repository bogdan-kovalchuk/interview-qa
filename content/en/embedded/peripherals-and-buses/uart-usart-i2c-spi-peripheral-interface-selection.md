---
id: emb-periph-0018
title: "What UART, USART, I2C, and SPI characteristics matter when choosing a peripheral interface?"
description: "UART is simple point-to-point serial, I2C adds addressable multi-drop at lower speed, and SPI is fast with chip select but no standard addressing."
track: embedded
section: peripherals-and-buses
level: senior
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

**UART/USART** is a simple point-to-point async/sync serial, good for logs or simple links. **I2C** has an addressable multi-drop bus, but lower speed and sensitivity to pull-ups/capacitance. **SPI** is fast and electrically simple, but needs a chip select per slave and has no standard addressing/error handling.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
