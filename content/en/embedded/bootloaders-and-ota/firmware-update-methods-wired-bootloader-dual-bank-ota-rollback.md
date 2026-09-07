---
id: emb-boot-0006
title: "What firmware update methods exist: wired flashing, bootloader, dual-bank, A/B image, OTA, and rollback?"
description: "Wired flashing suits factory use, a bootloader accepts images over serial or network, dual-bank or A/B preserves the working image, and rollback restores the last valid version after failure."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for bootloaders and ota concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Wired flashing** over SWD/JTAG/UART is simple for factory/service but not for field updates. A bootloader can accept an image over UART/USB/CAN/network; dual-bank or A/B allows writing a new image without erasing the working one. Rollback is needed to return to the previous valid version after a failed boot or health check.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
