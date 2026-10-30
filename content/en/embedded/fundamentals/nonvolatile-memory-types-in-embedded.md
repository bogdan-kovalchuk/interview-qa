---
id: emb-memlink-0010
title: "What types of non-volatile memory are used in embedded systems?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: ti-slaa526
    title: "Texas Instruments SLAA526: MSP430 FRAM Quality and Reliability"
    url: https://www.ti.com/lit/an/slaa526a/slaa526a.pdf
  - source_id: linux-mtd
    title: "Linux Kernel Documentation: Memory Technology Device (MTD) Subsystem"
    url: https://docs.kernel.org/driver-api/mtd/index.html
  - source_id: zephyr-nvs
    title: "Zephyr Project documentation: Non-Volatile Storage (NVS)"
    url: https://docs.zephyrproject.org/latest/services/storage/nvs/nvs.html
---

## Short answer

**NOR Flash** – byte-level reading, XIP (execute-in-place), addressable bus; used for firmware storage (MCU built-in Flash); slow block erase (~10K cycles).

**NAND Flash** – high density, cheaper; page-level reading only, not XIP (SD cards, eMMC, SSDs); requires FTL (flash translation layer).

**EEPROM** – byte-level erase/write, ~1M cycles; slow, small capacity; for configuration and settings.

**ROM / OTP** – written once or at manufacturing; bootloader in some MCUs.[^dou-embedded-interview]

## Detailed explanation

TODO
