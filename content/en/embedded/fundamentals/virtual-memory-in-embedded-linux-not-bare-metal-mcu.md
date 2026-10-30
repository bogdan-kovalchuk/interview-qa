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
  - source_id: love-linux-kernel-development
    title: "Robert Love: Linux Kernel Development, 3rd Edition. Addison-Wesley, 2010"
    url: https://www.pearson.com/en-us/subject-catalog/p/linux-kernel-development/P200000003468
  - source_id: armv7a-arm
    title: "ARMv7-A and ARMv7-R Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0406/latest/
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

Virtual memory gives each process its own address space, memory protection, lazy mapping, shared libraries, `mmap`, and copy-on-write. A bare-metal MCU typically has little RAM/Flash, deterministic requirements, and often only an MPU or no memory protection at all. Therefore it works with physical addresses, a linker script, and direct MMIO.[^dou-embedded-interview]

## Detailed explanation

TODO
