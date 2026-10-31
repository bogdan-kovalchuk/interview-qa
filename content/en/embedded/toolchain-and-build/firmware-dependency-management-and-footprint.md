---
id: emb-build-0020
title: "How do you manage dependencies in C/C++ firmware without accidentally pulling in non-portable or heap-heavy code?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Pin dependency versions, verify licenses, supported toolchains, heap/RTTI/exceptions usage, and footprint in the map file. Prefer explicitly adding small libraries with known configurations over pulling in a generic package with hidden POSIX, filesystem, or allocation assumptions. A **dependency review** for MCU must cover RAM/flash cost and behavior in an ISR/RTOS context.[^dou-embedded-interview]

## Detailed explanation

TODO
