---
id: emb-build-0020
title: "How do you manage C/C++ firmware dependencies without accidentally pulling in non-portable or heap-heavy code?"
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

Pin dependency versions, check licenses, supported toolchains, heap/RTTI/exceptions usage, and footprint in the map file. It is better to add small libraries with known configuration than to pull in a generic package with hidden POSIX, filesystem, or allocation assumptions. **Dependency review** for an MCU must include RAM/flash cost and behavior in ISR/RTOS context.[^dou-embedded-interview]

## Detailed explanation

TODO
