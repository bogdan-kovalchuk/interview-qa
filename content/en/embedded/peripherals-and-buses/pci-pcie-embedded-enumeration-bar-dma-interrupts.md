---
id: emb-periph-0021
title: "When can PCI/PCIe be an embedded topic and what basic concepts should you know: enumeration, BAR, DMA, interrupts?"
description: "PCI/PCIe appears on SoCs, industrial PCs, and FPGA cards; key concepts are enumeration, config space, BAR regions for MMIO, bus mastering DMA, and MSI/MSI-X interrupts."
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

PCI/PCIe becomes an embedded topic on SoCs, industrial computers, FPGA cards, high-speed peripherals, or Linux-based controllers. You need to know **enumeration**, config space, `BAR` regions for MMIO, bus mastering DMA, and MSI/MSI-X or legacy INTx interrupts. <span class="warn">The driver must map BAR correctly, manage DMA buffers, and account for IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
