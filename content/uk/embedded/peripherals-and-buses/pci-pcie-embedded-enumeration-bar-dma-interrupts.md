---
id: emb-periph-0021
title: "Коли PCI/PCIe може бути embedded-темою і які базові поняття треба знати: enumeration, BAR, DMA, interrupts?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

PCI/PCIe стає embedded-темою на SoC, industrial computers, FPGA cards, high-speed peripherals або Linux-based controllers. Потрібно знати **enumeration**, config space, `BAR` regions для MMIO, bus mastering DMA і interrupts MSI/MSI-X або legacy INTx. <span class="warn">Driver має правильно мапити BAR, керувати DMA buffers і враховувати IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
