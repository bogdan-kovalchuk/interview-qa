---
id: emb-conn-0006
title: "How does Bluetooth Classic differ from BLE in profiles, throughput, latency, and power consumption?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-architecture
    title: "Bluetooth Core Specification 6.0, Vol 1 Part A: Architecture"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/architecture,-change-history,-and-conventions/architecture.html
  - source_id: esp-idf-bt-overview
    title: "ESP-IDF Programming Guide: Bluetooth Architecture Overview"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/bt-architecture/overview.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-spp
    title: "Bluetooth SIG: Serial Port Profile 1.2"
    url: https://www.bluetooth.com/specifications/specs/serial-port-profile-1-2/
  - source_id: bt-a2dp
    title: "Bluetooth SIG: Advanced Audio Distribution Profile 1.4"
    url: https://www.bluetooth.com/specifications/specs/advanced-audio-distribution-profile-1-4/
  - source_id: bt-le-audio
    title: "Bluetooth SIG: LE Audio"
    url: https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/
---

## Short answer

**Bluetooth Classic** targets more persistent connections and profiles like audio/serial, often with higher throughput and greater power cost. **BLE** is optimized for short events, advertising, GATT data model and low consumption. For sensors/control BLE is usually better; for audio or legacy SPP, Classic is more often needed.[^dou-embedded-interview]

## Detailed explanation

TODO
