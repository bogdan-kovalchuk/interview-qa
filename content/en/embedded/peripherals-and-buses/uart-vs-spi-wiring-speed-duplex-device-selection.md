---
id: emb-periph-0011
title: "When is UART preferable to SPI when comparing wiring, speed, duplex, clocking, and device selection?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: linux-spi-summary
    title: "Linux kernel: Overview of Linux kernel SPI support"
    url: https://docs.kernel.org/spi/spi-summary.html
---

## Short answer

UART is simple: TX/RX/GND, asynchronous, good for console, modem, GPS and slower point-to-point links. SPI is faster, synchronous, full-duplex, but needs SCLK/MOSI/MISO and a separate CS per device or a decoder. For high-throughput sensor/display/flash on a board – often SPI; for a longer simple serial link without a shared clock – UART.[^dou-embedded-interview]

## Detailed explanation

TODO
