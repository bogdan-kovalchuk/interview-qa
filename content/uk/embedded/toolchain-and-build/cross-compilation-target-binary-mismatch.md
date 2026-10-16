---
id: emb-build-0017
title: "Що таке cross-compilation і які типові помилки виникають при запуску binary на іншій архітектурі?"
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

Cross-compilation – build на host-машині для іншого CPU/OS/ABI target. Типові помилки: зібрали під host, змішали wrong sysroot, soft/hard-float ABI, endian або libc, а потім отримали `Exec format error` чи runtime crash. Перевіряти треба `file`, `readelf -h`, target triplet і toolchain flags.[^dou-embedded-interview]

## Detailed explanation

TODO
