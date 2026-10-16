---
id: emb-build-0014
title: "What is an ELF file, and what information is useful to inspect in an embedded build?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

**ELF** is an object/executable format with headers, sections, symbols, relocations, and debug info. In embedded, one inspects the entry point, section sizes/addresses, symbol table, vector table placement, and whether `.data/.bss` landed in the correct RAM. Useful commands: `readelf -S`, `readelf -s`, `objdump -d`, `size`.[^dou-embedded-interview]

## Detailed explanation

TODO
