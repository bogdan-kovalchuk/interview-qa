---
id: emb-periph-0021
title: "Коли PCI/PCIe може бути embedded-темою і які базові поняття треба знати: enumeration, BAR, DMA, interrupts?"
description: "PCI/PCIe стає embedded-темою на SoC, industrial computers, FPGA cards, high-speed peripherals або Linux-based controllers. Потрібно знати enumeration, config space, BAR regions для MMIO, bus mastering DMA і interrupts MSI/MSI-X."
track: embedded
section: peripherals-and-buses
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

PCI/PCIe стає embedded-темою на SoC, industrial computers, FPGA cards, high-speed peripherals або Linux-based controllers. Потрібно знати **enumeration**, config space, `BAR` regions для MMIO, bus mastering DMA і interrupts MSI/MSI-X або legacy INTx. <span class="warn">Driver має правильно мапити BAR, керувати DMA buffers і враховувати IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
