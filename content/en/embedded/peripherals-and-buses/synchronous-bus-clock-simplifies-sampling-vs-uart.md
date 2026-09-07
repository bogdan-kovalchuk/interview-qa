---
id: emb-periph-0012
title: "What is the advantage of synchronous interfaces with a shared clock compared with asynchronous UART?"
description: "On a synchronous bus such as SPI or I2C the master supplies the clock, so the receiver need not recover bit timing from the baud rate."
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

On a synchronous bus such as SPI/I2C the master supplies the clock, so the receiver does not have to recover bit timing from the baud rate on its own. This simplifies sampling and allows higher speeds on short traces or a controlled board. UART is simpler in wiring, but more sensitive to baud mismatch, jitter and framing errors.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
