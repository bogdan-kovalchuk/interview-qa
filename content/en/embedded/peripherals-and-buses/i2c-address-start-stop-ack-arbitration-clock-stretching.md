---
id: emb-periph-0009
title: "How do devices communicate on I2C using addresses, start/stop, ACK/NACK, arbitration, and clock stretching?"
description: "An I2C master issues START, sends a 7- or 10-bit address plus the R/W bit, and receives ACK or NACK."
track: embedded
section: peripherals-and-buses
level: middle
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

The I2C master issues `START`, sends a 7/10-bit address plus the R/W bit, and the receiver responds with ACK or NACK. `STOP` ends the transaction; a repeated START allows a direction change without releasing the bus. Arbitration is needed for multi-master, and clock stretching lets a slave hold SCL low when it needs more time.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
