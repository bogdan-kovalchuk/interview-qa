---
id: emb-conn-0001
title: "How is the TCP/IP stack used in an IoT device, and where is the boundary between firmware, the OS, and the network stack?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: zephyr-net-stack-architecture
    title: "Zephyr Project documentation: Network Stack Architecture"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/net-stack-architecture.html
  - source_id: lwip-overview
    title: "lwIP 2.1.0: Overview"
    url: https://www.nongnu.org/lwip/2_1_x/index.html
  - source_id: lwip-pitfalls
    title: "lwIP 2.1.0: Common pitfalls"
    url: https://www.nongnu.org/lwip/2_1_x/pitfalls.html
  - source_id: lwip-multithreading
    title: "lwIP 2.1.0: Multithreading"
    url: https://www.nongnu.org/lwip/2_1_x/multithreading.html
  - source_id: esp-idf-lwip
    title: "ESP-IDF Programming Guide: lwIP"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/lwip.html
  - source_id: linux-napi
    title: "Linux kernel documentation: NAPI"
    url: https://docs.kernel.org/networking/napi.html
  - source_id: linux-man-tcp
    title: "tcp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/tcp.7.html
  - source_id: esp-at-overview
    title: "ESP-AT User Guide: What is ESP-AT"
    url: https://docs.espressif.com/projects/esp-at/en/latest/esp32/Get_Started/What_is_ESP-AT.html
  - source_id: zephyr-net-offload
    title: "Zephyr Project documentation: Network Traffic Offloading"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/net_offload.html
---

## Short answer

On a bare-metal MCU the TCP/IP stack is often provided by a library like lwIP, and the firmware directly controls the Ethernet/Wi-Fi driver and sockets-like API. In Embedded Linux the kernel contains the network stack and drivers, and the application works through the socket API. The boundary is where a frame from the hardware driver becomes a packet for the stack, and then an application protocol like MQTT/HTTP runs on top of TCP/TLS.[^dou-embedded-interview]

## Detailed explanation

TODO
