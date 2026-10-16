---
id: emb-fund-0025
title: "How to choose between MCU, DSP, FPGA, or an analog controller for a power control task?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**MCU** suits control logic, communication and moderate loops; **DSP** – for fast numerical control algorithms. **FPGA** provides parallelism and deterministic sub-microsecond timing, but is more expensive to develop. An analog controller is appropriate when simple, very fast or fail-safe regulation is needed without firmware dependency.[^dou-embedded-interview]

## Detailed explanation

TODO
