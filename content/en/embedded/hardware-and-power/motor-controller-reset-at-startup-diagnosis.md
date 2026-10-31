---
id: emb-hwbasic-0003
title: "A motor controller resets at startup. Which software, power-integrity, and hardware causes should you check?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-hwinfo
    title: "Zephyr Project documentation: Hardware Information"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/hwinfo.html
  - source_id: ti-drv8231a
    title: "TI DRV8231A 3.7-A Brushed DC Motor Driver with Integrated Current Sense and Regulation"
    url: https://www.ti.com/lit/ds/symlink/drv8231a.pdf
  - source_id: ti-slva714-smart-gate-drive
    title: "TI SLVA714: Understanding Smart Gate Drive"
    url: https://www.ti.com/lit/an/slva714/slva714.pdf
---

## Short answer

Software: brown-out/reset flags, watchdog, startup current path, PWM ramp, fault handlers and stack overflow. Power integrity: supply sag at inrush/stall current, ground bounce, weak regulator, poor decoupling and EMI from the motor. Hardware: driver shoot-through, flyback/TVS, high-current loop layout; probe Vcc/reset line with an oscilloscope right at the moment of startup.[^dou-embedded-interview]

## Detailed explanation

TODO
