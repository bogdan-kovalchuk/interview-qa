---
id: emb-periph-0013
title: "The encoder produces many pulses and the MCU hangs at high RPM. How do you estimate interrupt rate, debounce, timer capture, and CPU load?"
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

Calculate edge rate: pulses per revolution × RPM × edges per pulse, and compare with ISR time. If ISR on each edge takes a significant portion of CPU, switch to timer encoder mode/input capture, DMA, or a hardware counter. <span class="warn">Debounce delays in an ISR only make things worse</span>; for a mechanical encoder, use hardware/filter or a non-blocking state machine.[^dou-embedded-interview]

## Detailed explanation

TODO
