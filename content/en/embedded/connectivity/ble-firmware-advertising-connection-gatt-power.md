---
id: emb-conn-0005
title: "How does BLE work from the embedded firmware perspective: advertising interval, connection parameters, GATT, and power budget?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-core-hci
    title: "Bluetooth Core Specification 6.0, Vol 4 Part E: Host Controller Interface Functional Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host-controller-interface/host-controller-interface-functional-specification.html
  - source_id: bt-core-gap
    title: "Bluetooth Core Specification 6.0, Vol 3 Part C: Generic Access Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-access-profile.html
  - source_id: bt-core-att
    title: "Bluetooth Core Specification 6.0, Vol 3 Part F: Attribute Protocol"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/attribute-protocol--att-.html
  - source_id: bt-core-architecture
    title: "Bluetooth Core Specification 6.0, Vol 1 Part A: Architecture"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/architecture,-change-history,-and-conventions/architecture.html
  - source_id: bt-core-gatt
    title: "Bluetooth Core Specification 6.0, Vol 3 Part G: Generic Attribute Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-attribute-profile--gatt-.html
---

## Short answer

In BLE, a device advertises with an **advertising interval**, and after connection operates with negotiated connection interval, latency and supervision timeout. **GATT** defines services/characteristics for data and commands. Power budget depends heavily on radio wakeups, payload size, connection parameters, sleep states, and whether the firmware promptly returns the MCU to low power.[^dou-embedded-interview]

## Detailed explanation

TODO
