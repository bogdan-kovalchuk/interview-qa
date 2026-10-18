---
id: emb-hwbasic-0002
title: "What kinds of microcontrollers have you worked with?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

The answer is individual, but it is worth mentioning MCU families and their features:[^dou-embedded-interview]

- **ARM Cortex-M**: STM32 (F1/F4/H7) – most common in industry; HAL and LL libraries, CubeMX.
- **AVR**: ATmega328 (Arduino Uno) – 8-bit, easy start, well documented.
- **ESP32**: Wi-Fi/BT, dual-core Xtensa LX6, FreeRTOS – IoT applications.
- **RP2040**: dual-core ARM M0+, PIO for flexible peripheral I/O.

At an interview: name the MCU, describe which peripheral block you configured (UART/SPI/DMA/PWM) and for what task.

## Detailed explanation

TODO
