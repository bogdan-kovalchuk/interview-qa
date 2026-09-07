---
id: emb-periph-0004
title: "How does UART communication work?"
description: "UART sends a frame as a START bit, data bits, optional parity, and a STOP bit; the receiver synchronizes on the START edge."
track: embedded
section: peripherals-and-buses
level: junior
type: mechanism
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

The line is held HIGH in the IDLE state.[^dou-embedded-interview] Transmitter:

- Pulls the line LOW for 1 bit-time – this is the **START bit**
- Sends data bits, usually 8, though 5–9 are possible depending on hardware/configuration
- Optional: parity bit
- Raises the line HIGH – this is the **STOP bit**

The receiver synchronizes on the START edge and samples the line in the middle of each bit-time. If the baud rates differ, the data will be corrupted. TX of one side connects to RX of the other; a shared GND is mandatory.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
