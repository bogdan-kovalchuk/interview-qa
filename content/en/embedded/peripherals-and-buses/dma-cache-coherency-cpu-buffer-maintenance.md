---
id: emb-periph-0010
title: "What is DMA, and what problems can occur between DMA, the cache, and the CPU?"
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

**DMA** transfers data between a peripheral and memory without the CPU copying every byte. The problem is that the CPU cache may hold stale or not-yet-written data while DMA sees RAM directly. Before TX a cache clean/flush is needed; after RX – invalidate; plus proper alignment, memory barriers and buffers in DMA-accessible memory.[^dou-embedded-interview]

## Detailed explanation

TODO
