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
---

## Short answer

**Inter-Integrated Circuit** – a synchronous serial interface.[^dou-embedded-interview] Only two wires: `SCL` (clock) and `SDA` (data), both open-drain + pull-up resistors.

Key point: devices on the bus can only **pull the line low**; the HIGH level is produced by the pull-up resistor. This lets multiple devices share one bus safely.

Multi-master, multi-slave; Each slave has a unique 7-bit address; Half-duplex; Speeds: 100 kHz, 400 kHz, 1 MHz; ACK/NACK supported; Typical: sensors, EEPROM, RTC, OLED.

## Detailed explanation

TODO
