---
id: emb-cemb-0017
title: "What is alignment used for, and can it be controlled?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Alignment is needed for fast and correct CPU access to data.[^dou-embedded-interview] Many architectures read 2/4/8-byte values more efficiently when the address is a multiple of the type size; some MCUs can generate a fault on misaligned access.

You can control it through field order in a struct, standard `alignas` in C++ or `_Alignas`/`alignas` in modern C, and compiler-specific attributes like `__attribute__((aligned))`, `__attribute__((packed))`, `#pragma pack`. `packed` should be used carefully: it saves bytes but can slow down access or break hardware requirements.

## Detailed explanation

TODO
