---
id: emb-build-0022
title: "How do you configure CI to build firmware for multiple target platforms and toolchains?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

CI uses a **target x toolchain x config** matrix: for example GCC/Clang, debug/release, board variants. Each job installs a pinned toolchain, runs configure/build, static analysis, and unit tests, then collects artifacts: ELF, HEX/BIN, map, and logs. For target-only checks, HIL runners or nightly hardware jobs are attached separately.[^dou-embedded-interview]

## Detailed explanation

TODO
