---
id: emb-periph-0017
title: "How do you determine when UART/RS485 transmission is complete before switching the bus driver to receive?"
description: "Wait for transmission complete, when both the TX buffer and the shift register are empty, not just for the TX buffer empty flag."
track: embedded
section: peripherals-and-buses
level: senior
type: pitfall
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

Wait not only for an empty TX buffer but for **transmission complete**: the shift register must also be empty. In practice this is a flag like `TC`, an interrupt/DMA complete plus a UART TC check, or a timer guard time for the protocol. <span class="warn">`TXE` often means only that the data register is ready, not that the last bit has finished on the wire.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
