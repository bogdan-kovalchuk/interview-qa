---
id: emb-fund-0022
title: "Які типи пристроїв існують у Linux kernel і як вони представлені через device model?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

У Linux є **character**, **block**, **network**, platform, bus-specific devices тощо. Device model представляє їх через `struct device`, bus, driver, class і sysfs nodes. Для embedded важливі platform devices, devicetree/ACPI опис hardware і binding driver до compatible/resource data.[^dou-embedded-interview]

## Detailed explanation

TODO
