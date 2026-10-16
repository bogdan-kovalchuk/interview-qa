---
id: emb-fund-0011
title: "Why is virtual memory used in Embedded Linux, and why is it usually absent on a bare-metal MCU?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Virtual memory gives each process its own address space, memory protection, lazy mapping, shared libraries, `mmap`, and copy-on-write. A bare-metal MCU typically has little RAM/Flash, deterministic requirements, and often only an MPU or no memory protection at all. Therefore it works with physical addresses, a linker script, and direct MMIO.[^dou-embedded-interview]

## Detailed explanation

TODO
