---
id: emb-memlink-0015
title: "What does the linker do, and how does it place .text, .rodata, .data, .bss, stack, and heap?"
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

**Linker** resolves symbols/relocations, pulls the needed objects from libraries and places sections into memory regions. Typically `.text`/`.rodata` go into Flash, `.data` has a load image in Flash and a runtime address in RAM, `.bss` is zero-initialized in RAM. Stack/heap boundaries are set by the linker script or startup code, and a mistake here causes a hard fault or corruption.[^dou-embedded-interview]

## Detailed explanation

TODO
