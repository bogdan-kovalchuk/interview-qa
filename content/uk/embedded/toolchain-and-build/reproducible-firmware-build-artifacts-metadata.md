---
id: emb-build-0023
title: "Як організувати reproducible firmware build з pinned toolchain, artifacts, map file і version metadata?"
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

Зафіксуй toolchain version, build container або package hash, CMake presets/options і dependency versions. У artifacts зберігай `.elf`, `.hex`/`.bin`, `.map`, symbol/version info, compiler flags і commit hash. **Version metadata** у firmware має дозволяти точно відтворити binary, який стоїть на пристрої.[^dou-embedded-interview]

## Detailed explanation

TODO
