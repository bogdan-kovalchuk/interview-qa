---
id: emb-boot-0001
title: "What is a device tree?"
description: "A device tree is a data structure that describes board hardware separately from kernel code, allowing one Linux kernel image to support different boards."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for bootloaders and ota concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Device Tree** is a data structure that describes board hardware (CPU, memory, peripherals, interrupts, buses) in a kernel-code-independent form.[^dou-embedded-interview] It allows a single Linux kernel image to support different boards.

Files: `.dts` (Device Tree Source, text) is compiled by `dtc` into `.dtb` (Device Tree Blob, binary). The bootloader (U-Boot) passes the DTB address to the kernel at boot.

Example node: describes UART1 – base register address, interrupt number, clocking; the kernel driver reads these parameters through the DT API.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
