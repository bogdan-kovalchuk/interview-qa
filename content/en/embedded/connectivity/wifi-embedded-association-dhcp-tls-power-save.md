---
id: emb-conn-0007
title: "How does Wi-Fi work on an embedded device and what are the implications of association, DHCP, TLS, and power save modes?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: esp-idf-wifi-station
    title: "ESP-IDF Programming Guide: Wi-Fi Driver, Station Scenarios"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/wifi-driver/station-scenarios.html
  - source_id: rfc-2131-dhcp
    title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: https://www.rfc-editor.org/rfc/rfc2131.html
  - source_id: rfc-8446-tls13
    title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: https://www.rfc-editor.org/rfc/rfc8446.html
  - source_id: rfc-5280-x509
    title: "RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile"
    url: https://www.rfc-editor.org/rfc/rfc5280.html
  - source_id: rfc-8449-record-size-limit
    title: "RFC 8449: Record Size Limit Extension for TLS"
    url: https://www.rfc-editor.org/rfc/rfc8449.html
  - source_id: esp-idf-wifi-power
    title: "ESP-IDF Programming Guide: Wi-Fi Driver, Performance and Power Save"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/wifi-driver/wifi-performance-and-power-save.html
  - source_id: rfc-826-arp
    title: "RFC 826: An Ethernet Address Resolution Protocol"
    url: https://www.rfc-editor.org/rfc/rfc826.html
---

## Short answer

Embedded Wi-Fi goes through scan/auth/association with an AP, then obtains an IP via DHCP or static config. TLS adds CPU/RAM cost, certificates, entropy and long handshakes, which matters for a small MCU. Power save modes reduce consumption but add latency, buffering at the AP, and more complex reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

TODO
