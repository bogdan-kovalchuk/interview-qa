---
id: emb-conn-0001
title: "Як TCP/IP стек використовується в IoT-пристрої і де проходить межа між firmware, OS і network stack?"
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

На bare-metal MCU TCP/IP часто дає бібліотека типу lwIP, а firmware напряму керує Ethernet/Wi-Fi driver і sockets-like API. В Embedded Linux kernel містить network stack і drivers, а application працює через socket API. Межа проходить там, де frame від hardware driver стає packet-ом stack-а, а далі application protocol типу MQTT/HTTP працює поверх TCP/TLS.[^dou-embedded-interview]

## Detailed explanation

TODO
