---
id: emb-build-0015
title: "What is a translation unit, and why can include files cause multiple definition or ODR problems?"
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
  - source_id: gcc-code-gen-options
    title: "GCC manual: Options for Code Generation Conventions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html
  - source_id: gcc-10-changes
    title: "GCC 10 Release Series: Changes, New Features, and Fixes"
    url: https://gcc.gnu.org/gcc-10/changes.html
---

## Short answer

A **translation unit** is the result of preprocessing a single `.c/.cpp` file together with all its included headers. If a header contains a non-static object/function definition, it lands in every translation unit, and the linker sees multiple definitions. In C++, this can also violate the ODR; headers should retain only declarations, `inline`/`constexpr`, or templates according to language rules.[^dou-embedded-interview]

## Detailed explanation

TODO
