---
id: emb-conn-0012
title: "What sits between the network interface and the MCU: PHY, MAC, transceiver, controller, DMA, and driver stack?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-phy-abstraction
    title: "Linux kernel documentation: PHY Abstraction Layer"
    url: https://docs.kernel.org/networking/phy.html
  - source_id: linux-dma-api-howto
    title: "Linux kernel documentation: Dynamic DMA mapping Guide"
    url: https://docs.kernel.org/core-api/dma-api-howto.html
  - source_id: ti-dp83848c-datasheet
    title: "TI DP83848C PHYTER Single Port 10/100 Mb/s Ethernet Physical Layer Transceiver"
    url: https://www.ti.com/lit/ds/symlink/dp83848c.pdf
  - source_id: ti-sloa101-can
    title: "TI SLOA101B: Introduction to the Controller Area Network (CAN)"
    url: https://www.ti.com/lit/an/sloa101b/sloa101b.pdf
---

## Short answer

The physical medium is handled by a **PHY/transceiver**, which converts electrical/radio signals into digital link signals. A **MAC/controller** forms frames, filters, interrupts and often works with DMA descriptors in RAM. The driver stack initializes the hardware, manages buffers/cache coherency, handles IRQs and passes packets to the TCP/IP or fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

TODO
