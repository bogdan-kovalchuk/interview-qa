---
id: emb-memlink-0010
title: "Які типи постійної пам'яті використовуються в Embedded?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**NOR Flash** – побайтове читання, XIP (execute-in-place), адресована шина; використовується для зберігання firmware (MCU вбудована Flash).[2] Повільне стирання блоками (~10K циклів).

**NAND Flash** – висока щільність, дешевший; лише посторінкове читання, не XIP.[2] SD-карти, eMMC, SSD; потребує FTL (flash translation layer).

**EEPROM** – байтове стирання/запис, ~1M циклів; повільний, малий обсяг; для конфігурацій і налаштувань.

**ROM / OTP** – записується одноразово або при виробництві; bootloader у деяких MCU.[^dou-embedded-interview]

## Detailed explanation

TODO
