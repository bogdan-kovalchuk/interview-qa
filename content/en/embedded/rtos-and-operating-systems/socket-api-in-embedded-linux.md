---
id: emb-fund-0015
title: "What is a socket in Linux, and when does an embedded device actually need the socket API?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Socket** is a file descriptor for a network or local-IPC endpoint. An embedded device needs the socket API when it speaks TCP/UDP, Unix domain IPC, Bluetooth sockets, or has a daemon/client architecture. For a simple sensor-to-MCU link without an OS, a socket is not needed; there you get UART/SPI/I2C or a lightweight network stack API.[^dou-embedded-interview]

## Detailed explanation

TODO
