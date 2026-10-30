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
  - source_id: ti-c2000-real-time-mcu
    title: "Texas Instruments SPRUIV6: Getting Started With C2000 Real-Time Control Microcontrollers"
    url: https://www.ti.com/lit/ug/spruiv6/spruiv6.pdf
  - source_id: uc3842-datasheet
    title: "Texas Instruments UCx84x Current-Mode PWM Controllers Data Sheet"
    url: https://www.ti.com/lit/ds/symlink/uc3842.pdf
  - source_id: xilinx-xapp808
    title: "Xilinx Application Note XAPP808: FPGA Motor Control Reference Design"
    url: https://docs.amd.com/v/u/en-US/xapp808
---

## Short answer

**MCU** suits control logic, communication and moderate loops; **DSP** – for fast numerical control algorithms. **FPGA** provides parallelism and deterministic sub-microsecond timing, but is more expensive to develop. An analog controller is appropriate when simple, very fast or fail-safe regulation is needed without firmware dependency.[^dou-embedded-interview]

## Detailed explanation

TODO
