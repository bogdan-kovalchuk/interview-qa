---
id: emb-periph-0015
title: "How do you read 256 channels when the MCU has only 8 GPIOs, and what are the trade-offs of multiplexers, shift registers, and an external ADC?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: ti-sn74hc165
    title: "TI SNx4HC165 8-Bit Parallel-Load Shift Registers"
    url: https://www.ti.com/lit/ds/symlink/sn74hc165.pdf
  - source_id: ti-cd74hc4067
    title: "TI CD74HCx4067 High-Speed CMOS Logic 16-Channel Analog Multiplexer and Demultiplexer"
    url: https://www.ti.com/lit/ds/symlink/cd74hc4067.pdf
  - source_id: ti-sn74hc138
    title: "TI SNx4HC138 3-Line To 8-Line Decoders/Demultiplexers"
    url: https://www.ti.com/lit/ds/symlink/sn74hc138.pdf
---

## Short answer

For digital inputs, cascade shift registers or GPIO expanders over SPI/I2C; for analog, use analog multiplexers or an external multi-channel ADC. A multiplexer saves pins but needs settling time and sequential sampling; a shift register is fast for digital but cannot read analog. An external ADC gives better accuracy and sampling isolation, but adds cost, bus bandwidth, and driver complexity.[^dou-embedded-interview]

## Detailed explanation

TODO
