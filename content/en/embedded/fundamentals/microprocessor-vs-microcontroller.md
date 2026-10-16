---
id: emb-fund-0008
title: "What is the difference between a microprocessor and a microcontroller?"
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

**Microprocessor (MPU)** is primarily a CPU that usually requires external RAM, Flash, and peripherals.[^dou-embedded-interview] High performance, more often runs a full OS; examples: Intel Core, ARM Cortex-A.

**Microcontroller (MCU)** – CPU + Flash + RAM + GPIO/UART/SPI/ADC/timers on a single chip. Low power, cheaper, deterministic behavior; many MCUs such as ARM Cortex-M use **modified Harvard architecture**, but not all MCUs should strictly be called Harvard.

Choice: MPU for an OS and complex computation; MCU for real-time hardware control.

## Detailed explanation

TODO
