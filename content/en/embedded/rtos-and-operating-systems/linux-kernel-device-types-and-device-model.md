---
id: emb-fund-0022
title: "Which device types exist in the Linux kernel, and how are they represented by the device model?"
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

Linux has **character**, **block**, **network**, platform, and bus-specific devices, among others. The device model represents them through `struct device`, bus, driver, class, and sysfs nodes. For embedded, platform devices, devicetree/ACPI hardware description, and driver binding to compatible/resource data are important.[^dou-embedded-interview]

## Detailed explanation

TODO
