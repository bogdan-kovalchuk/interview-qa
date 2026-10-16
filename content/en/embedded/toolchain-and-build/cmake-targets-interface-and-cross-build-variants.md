---
id: emb-build-0021
title: "How can CMake describe dependencies, targets, interface include directories, and cross-platform build variants?"
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

In CMake, every library/application must be a **target** with its own sources, compile definitions, include dirs, and link dependencies. `target_include_directories(... INTERFACE)` publishes headers to consumers, while `PRIVATE` keeps them local. Cross-build variants are set via a toolchain file, presets, target-specific options, and separate targets for the MCU, host tests, and utilities.[^dou-embedded-interview]

## Detailed explanation

TODO
