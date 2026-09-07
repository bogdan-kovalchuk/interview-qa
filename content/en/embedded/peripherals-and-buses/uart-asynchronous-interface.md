---
id: emb-periph-0008
title: "What is UART?"
description: "UART is an asynchronous serial interface with TX/RX, an agreed baud rate, and frames of start, data, optional parity, and stop bits."
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

**Universal Asynchronous Receiver-Transmitter** – an asynchronous serial interface. Two wires: `TX` (transmit) and `RX` (receive). No shared clock – both devices agree on the **baud rate** in advance (e.g. 115200 baud).[^dou-embedded-interview]

Frame: START bit -> data bits -> parity (optional) -> STOP bit(s); Typically 8 data bits are used, though hardware/configuration may support 5–9; UART describes data framing; electrical levels can be TTL/CMOS, RS-232, RS-485, etc.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
