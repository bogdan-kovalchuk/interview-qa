---
id: emb-periph-0016
title: "How does RS485 half-duplex work, and how should the DE/RE pins be controlled during transmit and receive?"
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

RS485 half-duplex shares a differential bus, so a device either transmits or listens. Before transmit, enable the driver via `DE`; usually disable the receiver via `RE` or leave it for an echo-check; after the transmission completes fully, return to receive. <span class="warn">Switching too early truncates the stop bit; switching too late blocks another node's response.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
