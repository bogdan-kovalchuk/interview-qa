---
id: emb-memlink-0010
title: "What types of non-volatile memory are used in embedded systems?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**NOR Flash** – byte-level reading, XIP (execute-in-place), addressable bus; used for firmware storage (MCU built-in Flash).[2] Slow block erase (~10K cycles).

**NAND Flash** – high density, cheaper; page-level reading only, not XIP.[2] SD cards, eMMC, SSDs; requires FTL (flash translation layer).

**EEPROM** – byte-level erase/write, ~1M cycles; slow, small capacity; for configuration and settings.

**ROM / OTP** – written once or at manufacturing; bootloader in some MCUs.[^dou-embedded-interview]

## Detailed explanation

TODO
