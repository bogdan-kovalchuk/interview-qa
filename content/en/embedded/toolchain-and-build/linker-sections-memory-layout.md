---
id: emb-memlink-0015
title: "What does the linker do, and how does it place the .text, .rodata, .data, .bss, stack, and heap sections?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

The **linker** resolves symbols/relocations, pulls needed objects from libraries, and places sections in memory regions. Typically `.text`/`.rodata` go to Flash, `.data` has a load image in Flash and runtime address in RAM, and `.bss` is zero-initialized in RAM. Stack/heap boundaries are set by the linker script or startup code, and an error here causes hard faults or corruption.[^dou-embedded-interview]

## Detailed explanation

TODO
