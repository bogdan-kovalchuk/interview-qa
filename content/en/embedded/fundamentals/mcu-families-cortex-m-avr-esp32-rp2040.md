---
id: emb-hwbasic-0002
title: "What kinds of microcontrollers have you worked with?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: espressif-esp32-trm
    title: "ESP32 Technical Reference Manual"
    url: https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf
  - source_id: raspberrypi-rp2040-datasheet
    title: "RP2040 Datasheet: A microcontroller by Raspberry Pi"
    url: https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf
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
