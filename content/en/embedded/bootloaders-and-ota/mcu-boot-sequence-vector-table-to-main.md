---
id: emb-boot-0003
title: "How does program loading work in a microcontroller?"
description: "After reset the Cortex-M hardware reads the vector table, loads SP and the reset handler, startup code copies .data and clears .bss, clocks are initialized, and main() is called."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for bootloaders and ota concepts; details of specific devices and toolchains can differ."
---

## Short answer

After power-on or reset (ARM Cortex-M):[^dou-embedded-interview]

- Hardware reads the **Vector Table** from address `0x00000000` (Flash)
- Loads the initial SP value from the word at `0x00000000`
- Loads the Reset Handler address into PC from `0x00000004`
- **Startup code** (crt0 / startup.s) copies the `.data` section from Flash to RAM, fills `.bss` with zeros
- Initializes clocking (PLL, clock tree)
- Calls `main()`.

The program is stored in **Flash (non-volatile)**, executed from there or copied to RAM (XIP or execute-in-place).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
