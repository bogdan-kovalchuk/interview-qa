---
id: emb-conn-0013
title: "Which industrial or vision interfaces can be embedded-relevant but niche: EtherCAT, FPD-Link III, MIPI CSI, GigE Vision, USB3 Vision?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: ethercat-technology
    title: "EtherCAT Technology Group: EtherCAT Technology"
    url: https://www.ethercat.org/en/technology.html
  - source_id: ti-ds90ub954-q1
    title: "TI DS90UB954-Q1 Dual 4.16 Gbps FPD-Link III Deserializer Hub With MIPI CSI-2 Outputs"
    url: https://www.ti.com/lit/ds/symlink/ds90ub954-q1.pdf
  - source_id: linux-v4l2-tx-rx
    title: "Linux kernel documentation: Pixel data transmitter and receiver drivers"
    url: https://docs.kernel.org/driver-api/media/tx-rx.html
  - source_id: a3-gige-vision
    title: "A3: GigE Vision Standard"
    url: https://www.automate.org/vision/vision-standards/vision-standards-gige-vision
  - source_id: a3-usb3-vision
    title: "A3: What Is USB3 Vision?"
    url: https://www.automate.org/vision/vision-standards/usb3-vision
  - source_id: aravis-ethernet-performance
    title: "Aravis documentation: Ethernet Devices"
    url: https://aravisproject.github.io/aravis/aravis-stable/ethernet.html
---

## Short answer

**EtherCAT** is deterministic industrial Ethernet for motion/control, often with a dedicated slave controller. **FPD-Link III** and **MIPI CSI** appear frequently in camera/display pipelines on embedded SoC. **GigE Vision** and **USB3 Vision** are machine-vision transports where bandwidth, latency, drivers and buffer handling matter.[^dou-embedded-interview]

## Detailed explanation

TODO
