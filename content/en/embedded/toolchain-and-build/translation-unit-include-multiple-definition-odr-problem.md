---
id: emb-build-0015
title: "What is a translation unit, and why can include files cause multiple-definition or ODR problems?"
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

**Translation unit** is the result of preprocessing one `.c/.cpp` file together with all included headers. If a header contains a non-static object or function definition, it ends up in every translation unit and the linker sees multiple definitions. In C++ this can also violate the ODR; headers should contain only declarations, `inline`/`constexpr`, or templates as the language rules allow.[^dou-embedded-interview]

## Detailed explanation

TODO
