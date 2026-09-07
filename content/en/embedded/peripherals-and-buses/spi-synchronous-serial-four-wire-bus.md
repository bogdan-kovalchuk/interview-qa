---
id: emb-periph-0001
title: "What is `SPI`?"
description: "SPI is a synchronous full-duplex serial interface on four lines with no addressing and no ACK."
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

**Serial Peripheral Interface** – a synchronous serial interface. Four lines: `SCK` (clock), `MOSI` (Master Out Slave In), `MISO` (Master In Slave Out), `CS/SS` (Chip Select, active LOW).

Master-slave architecture. Full duplex. High speed (tens of MHz); Separate CS for each slave; No addressing – device selection via CS; No ACK; Typical: Flash memory, ADCs, displays, SD cards.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
