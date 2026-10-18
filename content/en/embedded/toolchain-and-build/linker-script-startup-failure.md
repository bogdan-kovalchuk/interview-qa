---
id: emb-memlink-0016
title: "What is a linker script, and which errors can break firmware startup?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**Linker script** describes Flash/RAM regions, entry point, sections, vector table and symbols for startup. Typical errors: wrong vector table address, overlap of `.data/.bss/heap/stack`, unexported `_sidata/_sdata/_edata/_sbss/_ebss`, incorrect RAM origin/length. <span class="warn">Such errors often appear as a reset loop or HardFault before main</span>.[^dou-embedded-interview]

## Detailed explanation

TODO
