---
id: emb-cemb-0039
title: "Why do C99 and C11 matter for embedded C, and which C11 features may be unavailable in MCU toolchains?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

C99 brought `stdint.h`, `stdbool.h`, designated initializers, mixed declarations, and `inline`, which are very useful for embedded. C11 added atomics, threads, alignment features, and static assertions. <span class="warn">On MCU toolchains C11 threads/atomics may be incomplete or depend on the runtime/libc</span>, so the specific compiler and flags must be checked.[^dou-embedded-interview]

## Detailed explanation

TODO
