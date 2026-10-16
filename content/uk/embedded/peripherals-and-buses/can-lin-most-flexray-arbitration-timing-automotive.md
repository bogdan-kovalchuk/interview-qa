---
id: emb-periph-0019
title: "Як працюють CAN, LIN, MOST і FlexRay, і чим вони відрізняються за arbitration, timing і automotive use-case?"
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

**CAN** має multi-master arbitration за message ID і добре підходить для robust control networks. **LIN** дешевший master-slave bus для простих actuators/sensors; **FlexRay** дає deterministic time-triggered communication для safety-critical systems. **MOST** історично використовувався для automotive multimedia; його роль інша, ніж у control buses.[^dou-embedded-interview]

## Detailed explanation

TODO
