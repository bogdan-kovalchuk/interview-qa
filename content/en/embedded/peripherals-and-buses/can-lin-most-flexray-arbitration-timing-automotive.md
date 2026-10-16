---
id: emb-periph-0019
title: "How do CAN, LIN, MOST, and FlexRay work, and how do they differ in arbitration, timing, and automotive use-case?"
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

**CAN** has multi-master arbitration by message ID and suits robust control networks. **LIN** is a cheaper master-slave bus for simple actuators/sensors; **FlexRay** provides deterministic time-triggered communication for safety-critical systems. **MOST** was historically used for automotive multimedia; its role differs from that of control buses.[^dou-embedded-interview]

## Detailed explanation

TODO
