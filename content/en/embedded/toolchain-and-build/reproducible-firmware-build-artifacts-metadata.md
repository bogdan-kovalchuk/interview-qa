---
id: emb-build-0023
title: "How do you organize a reproducible firmware build with a pinned toolchain, artifacts, map file, and version metadata?"
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
  - source_id: reproducible-builds-definition
    title: "Reproducible Builds: Definitions"
    url: https://reproducible-builds.org/docs/definition/
---

## Short answer

Pin the toolchain version, build container or package hash, CMake presets/options, and dependency versions. In artifacts, store `.elf`, `.hex`/`.bin`, `.map`, symbol/version info, compiler flags, and commit hash. **Version metadata** in firmware must allow exact recreation of the binary running on the device.[^dou-embedded-interview]

## Detailed explanation

TODO
