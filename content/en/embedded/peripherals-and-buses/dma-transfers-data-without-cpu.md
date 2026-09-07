---
id: emb-periph-0006
title: "What is DMA?"
description: "DMA transfers data between a peripheral and memory without continuous CPU involvement, reducing load and stabilizing timing."
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

**DMA (Direct Memory Access)** – a mechanism for transferring data between a peripheral and memory or between memory regions without continuous CPU involvement.[^dou-embedded-interview]

Example: UART RX or ADC writes data directly into a RAM buffer while the CPU only configures the DMA controller: peripheral address, buffer address, size, direction and mode. On completion the DMA can generate an interrupt.

Advantages: lower CPU load, higher throughput, more stable timing. Typical tasks: SPI/UART/I2C transfers, ADC sampling, audio buffers, display refresh.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
