---
id: emb-periph-0007
title: "What is I2C?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: nxp-um10204
    title: "NXP UM10204: I2C-bus specification and user manual"
    url: https://www.nxp.com/docs/en/user-guide/UM10204.pdf
---

## Short answer

**Inter-Integrated Circuit** – synchronous serial interface.[^dou-embedded-interview] Only two wires: `SCL` (clock) and `SDA` (data), both open-drain + pull-up resistors.

Key nuance: devices on the bus can only **pull the line down**; the HIGH state is formed by a pull-up resistor. This allows multiple devices to safely share one bus.

Multi-master, multi-slave; Each slave has a unique 7-bit address; Half-duplex; Speeds: 100 kHz, 400 kHz, 1 MHz; Has ACK/NACK; Typical: sensors, EEPROM, RTC, OLED.

## Detailed explanation

TODO
