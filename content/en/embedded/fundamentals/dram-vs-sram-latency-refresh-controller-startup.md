---
id: emb-dtypes-0105
title: "How does DRAM differ from SRAM and what are the implications for latency, refresh, controller, and startup?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: microchip-mpu-memory
    title: "Microchip Developer Help: Differences Between MCU and MPU Development"
    url: https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mpu/differences-between-mcu-and-mpu-development/
  - source_id: uboot-memory-startup
    title: "U-Boot documentation: Memory Management"
    url: https://docs.u-boot.org/en/latest/develop/memory.html
---

## Short answer

**SRAM** needs no refresh and usually has lower access latency, but its cost per bit is higher. **DRAM** provides greater density and capacity, but needs a memory controller and periodic refresh; access latency depends on the memory technology and access pattern.[^microchip-mpu-memory] On a board with external DRAM, early boot can run from SRAM until boot code configures the controller and DRAM.[^uboot-memory-startup]

## Detailed explanation

TODO
