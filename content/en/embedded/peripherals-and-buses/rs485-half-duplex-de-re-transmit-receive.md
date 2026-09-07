---
id: emb-periph-0016
title: "How does RS485 half-duplex work, and how should the DE/RE pins be controlled during transmit and receive?"
description: "In RS485 half-duplex, control DE and RE so the driver is enabled only during transmit and the bus returns to receive after the last bit has left the wire."
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

RS485 half-duplex shares a differential bus, so a device either transmits or listens. Before transmit, enable the driver via `DE`; usually disable the receiver via `RE` or leave it for an echo-check; after the transmission completes fully, return to receive. <span class="warn">Switching too early truncates the stop bit; switching too late blocks another node's response.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
