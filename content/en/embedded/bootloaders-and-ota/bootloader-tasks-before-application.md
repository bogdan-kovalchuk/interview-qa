---
id: emb-boot-0004
title: "What is an MCU bootloader, and what does it do before application firmware starts?"
description: "An MCU bootloader starts after reset, verifies or updates an image, selects a slot, and transfers control to application firmware."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for bootloaders and ota concepts; details of specific devices and toolchains can differ."
---

## Short answer

A bootloader is a small firmware that starts first after reset. It can verify an image signature/CRC, select a slot, update firmware over UART/USB/CAN/BLE, configure the vector table, and transfer control to the application. In safety/security systems it also manages rollback, anti-bricking, and chain of trust.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
