---
id: emb-periph-0006
title: "What is DMA?"
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

**DMA (Direct Memory Access)** – a mechanism for transferring data between a peripheral and memory or between memory regions without continuous CPU involvement.[^dou-embedded-interview]

Example: UART RX or ADC writes data directly into a RAM buffer while the CPU only configures the DMA controller: peripheral address, buffer address, size, direction and mode. On completion the DMA can generate an interrupt.

Advantages: lower CPU load, higher throughput, more stable timing. Typical tasks: SPI/UART/I2C transfers, ADC sampling, audio buffers, display refresh.

## Detailed explanation

TODO
