---
id: emb-boot-0005
title: "What happens during the MCU boot sequence from reset vector to main or scheduler start?"
description: "After reset the CPU loads SP and the reset handler from the vector table, startup code copies .data, clears .bss, runs constructors, enters main, and the firmware starts the scheduler."
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

After reset the CPU takes the initial stack pointer and reset handler from the vector table. Startup code sets up the low-level runtime: clock minimally or later, copies `.data` from flash to RAM, clears `.bss`, calls constructors in C++, and enters `main`. Then the firmware initializes HAL/drivers, interrupts, RTOS objects, and starts the scheduler.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
