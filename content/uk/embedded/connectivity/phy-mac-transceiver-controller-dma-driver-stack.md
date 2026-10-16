---
id: emb-conn-0012
title: "Що стоїть між network interface і MCU: PHY, MAC, transceiver, controller, DMA і driver stack?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Physical medium обслуговує **PHY/transceiver**, який перетворює electrical/radio signals у digital link signals. **MAC/controller** формує frames, filters, interrupts і часто працює з DMA descriptors у RAM. Driver stack ініціалізує hardware, керує buffers/cache coherency, обробляє IRQ і передає packets у TCP/IP або fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

TODO
