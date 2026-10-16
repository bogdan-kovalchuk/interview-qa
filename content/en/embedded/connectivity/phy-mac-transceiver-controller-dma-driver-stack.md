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
---

## Short answer

The physical medium is handled by a **PHY/transceiver**, which converts electrical/radio signals into digital link signals. A **MAC/controller** forms frames, filters, interrupts and often works with DMA descriptors in RAM. The driver stack initializes the hardware, manages buffers/cache coherency, handles IRQs and passes packets to the TCP/IP or fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

TODO
