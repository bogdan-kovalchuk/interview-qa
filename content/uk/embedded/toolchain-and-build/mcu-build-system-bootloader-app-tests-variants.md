---
id: emb-build-0024
title: "Як побудувати build system для MCU-проекту з bootloader, application, tests і hardware variants?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Розбий build на окремі targets: `bootloader`, `app`, shared drivers, host tests, target tests і board configs. Кожен target має свій linker script, startup file, compile definitions, memory layout і output artifacts. Hardware variants краще описувати через board files/config targets, а не умовні блоки у кожному source file.[^dou-embedded-interview]

## Detailed explanation

TODO
