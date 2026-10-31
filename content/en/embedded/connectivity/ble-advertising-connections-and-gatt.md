---
id: emb-conn-0003
title: "How does BLE work at the level of advertising, connections, GATT services, and characteristics?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-gap
    title: "Bluetooth Core Specification 6.0, Vol 3 Part C: Generic Access Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-access-profile.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-core-hci
    title: "Bluetooth Core Specification 6.0, Vol 4 Part E: Host Controller Interface Functional Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host-controller-interface/host-controller-interface-functional-specification.html
  - source_id: bt-core-att
    title: "Bluetooth Core Specification 6.0, Vol 3 Part F: Attribute Protocol"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/attribute-protocol--att-.html
  - source_id: bt-core-gatt
    title: "Bluetooth Core Specification 6.0, Vol 3 Part G: Generic Attribute Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-attribute-profile--gatt-.html
---

## Short answer

A BLE peripheral broadcasts advertising packets with an address, flags and optional service data, while a central scans and initiates a connection. After the connection the data model is usually GATT: services group characteristics, and a characteristic has a value and properties such as read/write/notify. For low-power telemetry the key parameters are connection interval, MTU, notification rate and sleep between events.[^dou-embedded-interview]

## Detailed explanation

TODO
