---
id: emb-periph-0013
title: "An encoder produces many pulses and the MCU hangs at high speed. How do you assess interrupt rate, debounce, timer capture, and CPU load?"
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

Calculate the edge rate: pulses per revolution × RPM × edges per pulse, and compare it with the ISR time. If an ISR on every edge takes a significant share of CPU, switch to timer encoder mode/input capture, DMA, or a hardware counter. <span class="warn">Debounce via ISR delays only makes things worse</span>; a mechanical encoder needs hardware/filter or a non-blocking state machine.[^dou-embedded-interview]

## Detailed explanation

TODO
