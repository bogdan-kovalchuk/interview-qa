---
id: emb-periph-0010
title: "What is DMA and what issues arise between DMA, cache, and the CPU?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

**DMA** transfers data between a peripheral and memory without the CPU copying every byte. The problem is that the CPU cache may hold dirty or stale data while DMA accesses RAM directly. Clean/flush the cache before TX, invalidate after RX, and ensure proper alignment, memory barriers, and buffers located in DMA-accessible memory.[^dou-embedded-interview]

## Detailed explanation

TODO
