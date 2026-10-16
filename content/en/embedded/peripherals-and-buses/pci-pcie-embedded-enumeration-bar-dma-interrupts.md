---
id: emb-periph-0021
title: "When can PCI/PCIe be an embedded topic and what basic concepts should you know: enumeration, BAR, DMA, interrupts?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

PCI/PCIe becomes an embedded topic on SoCs, industrial computers, FPGA cards, high-speed peripherals, or Linux-based controllers. You need to know **enumeration**, config space, `BAR` regions for MMIO, bus mastering DMA, and MSI/MSI-X or legacy INTx interrupts. <span class="warn">The driver must map BAR correctly, manage DMA buffers, and account for IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
