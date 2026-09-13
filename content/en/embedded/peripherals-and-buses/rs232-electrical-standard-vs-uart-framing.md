---
id: emb-periph-0003
title: "How does `RS232` communication work?"
description: "RS-232 is an electrical signal standard with inverted levels and longer range; UART describes data framing – they are different things."
track: embedded
section: peripherals-and-buses
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-13
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

RS-232 is an **electrical signal standard** and UART is the data-framing block, so they are not the same: UART describes the frame, baud rate and start/stop/parity bits, RS-232 the voltage levels and physical interface.

Differences from TTL UART:

- **Voltage levels**: logic 1 = −3 to −15 V, logic 0 = +3 to +15 V (inverted!), vs TTL 0/3.3–5 V;
- distance: up to ~15 m (TTL ~1 m);
- connector: DB-9 with `RTS`/`CTS` for flow-control;
- an MCU needs a level converter, e.g. `MAX232`.[^dou-embedded-interview]
## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
