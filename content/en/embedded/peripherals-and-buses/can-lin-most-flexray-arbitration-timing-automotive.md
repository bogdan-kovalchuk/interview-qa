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
  - source_id: iso-11898-1
    title: "ISO 11898-1: Road vehicles – Controller area network (CAN) – Part 1: Data link layer and physical signalling"
    url: https://www.iso.org/standard/63648.html
  - source_id: ti-sloa101-can
    title: "Texas Instruments SLOA101B: Introduction to the Controller Area Network (CAN)"
    url: https://www.ti.com/lit/an/sloa101b/sloa101b.pdf
  - source_id: lin-2-2a-spec
    title: "LIN Specification Package, Revision 2.2A"
    url: https://www.cs-group.de/wp-content/uploads/2016/11/LIN_Specification_Package_2.2A.pdf
---

## Short answer

**CAN** has multi-master arbitration by message ID and suits robust control networks. **LIN** is a cheaper master-slave bus for simple actuators/sensors; **FlexRay** provides deterministic time-triggered communication for safety-critical systems. **MOST** was historically used for automotive multimedia; its role differs from that of control buses.[^dou-embedded-interview]

## Detailed explanation

TODO
