---
id: emb-fund-0008
title: "What is the difference between a microprocessor and a microcontroller?"
description: "A microprocessor (MPU) is mainly a CPU needing external memory and peripherals for an OS, while a microcontroller (MCU) integrates CPU, Flash, RAM, and peripherals on one die."
track: embedded
section: fundamentals
level: junior
type: comparison
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Microprocessor (MPU)** is primarily a CPU that usually requires external RAM, Flash, and peripherals.[^dou-embedded-interview] High performance, more often runs a full OS; examples: Intel Core, ARM Cortex-A.

**Microcontroller (MCU)** – CPU + Flash + RAM + GPIO/UART/SPI/ADC/timers on a single chip. Low power, cheaper, deterministic behavior; many MCUs such as ARM Cortex-M use **modified Harvard architecture**, but not all MCUs should strictly be called Harvard.

Choice: MPU for an OS and complex computation; MCU for real-time hardware control.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
