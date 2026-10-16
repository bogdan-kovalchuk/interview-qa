---
id: emb-build-0014
title: "Що таке ELF-файл і яку інформацію в ньому корисно дивитися для embedded build?"
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

**ELF** – object/executable формат із headers, sections, symbols, relocations і debug info. В embedded дивляться entry point, section sizes/addresses, symbol table, vector table placement і чи `.data/.bss` потрапили в правильну RAM. Корисні команди: `readelf -S`, `readelf -s`, `objdump -d`, `size`.[^dou-embedded-interview]

## Detailed explanation

TODO
