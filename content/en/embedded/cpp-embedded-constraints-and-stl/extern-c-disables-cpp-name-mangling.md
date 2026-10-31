---
id: emb-cemb-0018
title: "What is extern \"C\" for?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

`extern "C"` is used in C++ to tell the compiler to apply C linkage to functions or variables.[^dou-embedded-interview] The main effect is disabling C++ name mangling, so the symbol name in the object/shared library will be C-compatible.

This is needed when C++ code calls a C library or C code needs to call a function written in C++. A typical header is written as: `#ifdef __cplusplus extern "C" { #endif` ... `#ifdef __cplusplus } #endif`, but the function body itself remains C++ code, while the ABI and symbol name become C-compatible.

## Detailed explanation

TODO
