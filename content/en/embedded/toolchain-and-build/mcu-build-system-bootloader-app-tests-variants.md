---
id: emb-build-0024
title: "How do you build a build system for an MCU project with a bootloader, application, tests, and hardware variants?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Split the build into distinct targets: `bootloader`, `app`, shared drivers, host tests, target tests, and board configs. Each target has its own linker script, startup file, compile definitions, memory layout, and output artifacts. Describe hardware variants through board files/config targets rather than conditional blocks in every source file.[^dou-embedded-interview]

## Detailed explanation

TODO
