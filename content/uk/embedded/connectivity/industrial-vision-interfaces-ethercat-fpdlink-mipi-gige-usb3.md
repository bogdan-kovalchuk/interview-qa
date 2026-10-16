---
id: emb-conn-0013
title: "Які industrial або vision interfaces можуть бути embedded-relevant, але нішевими: EtherCAT, FPD-Link III, MIPI CSI, GigE Vision, USB3 Vision?"
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

**EtherCAT** - deterministic industrial Ethernet для motion/control, часто з dedicated slave controller. **FPD-Link III** і **MIPI CSI** часто зустрічаються у camera/display pipelines на embedded SoC. **GigE Vision** і **USB3 Vision** - machine-vision transports, де важливі bandwidth, latency, drivers і buffer handling.[^dou-embedded-interview]

## Detailed explanation

TODO
