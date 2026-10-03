---
id: emb-dtypes-0105
title: "How does DRAM differ from SRAM and what are the implications for latency, refresh, controller, and startup?"
description: "SRAM needs no refresh and costs more per bit; DRAM is denser but needs a controller and refresh, while its latency depends on the system and access pattern."
track: embedded
section: data-types-and-memory-layout
level: senior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: microchip-mpu-memory
    title: "Microchip Developer Help: Differences Between MCU and MPU Development"
    url: https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mpu/differences-between-mcu-and-mpu-development/
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Compares typical SRAM and DRAM use, density, cost, and memory-controller role in the described Microchip MPU systems; it does not set universal latency values."
  - source_id: uboot-memory-startup
    title: "U-Boot documentation: Memory Management"
    url: https://docs.u-boot.org/en/latest/develop/memory.html
    accessed: 2026-10-04
    kind: official
    version: "latest"
    applicability: "Shows a boot-flow example where early memory may be SRAM before DRAM initialization and the stack can move after setup; exact order depends on the board."
---

## Short answer

**SRAM** needs no refresh and usually has lower access latency, but its cost per bit is higher. **DRAM** provides greater density and capacity, but needs a memory controller and periodic refresh; access latency depends on the memory technology and access pattern.[^microchip-mpu-memory] On a board with external DRAM, early boot can run from SRAM until boot code configures the controller and DRAM.[^uboot-memory-startup]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
