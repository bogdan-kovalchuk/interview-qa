---
id: emb-fund-0017
title: "How does Harvard architecture differ from von Neumann, and how does this affect Flash/RAM access?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
---

## Short answer

In **von Neumann**, code and data share one address space/bus. In **Harvard**, instruction and data memories/buses are separate, so Flash and RAM can have different access rules. On some MCUs, reading constants from program memory requires special instructions/API, and self-programming Flash has erase/write and timing limitations.[^dou-embedded-interview]

## Detailed explanation

TODO
