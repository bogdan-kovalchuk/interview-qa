---
id: emb-build-0018
title: "How do compiler optimization levels affect timing, debugging, and undefined behavior in firmware?"
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

Higher `-O` levels change instruction order, inlining, register allocation, and timing, so delay loops, race conditions, and undefined behavior may manifest differently. Debugging becomes harder: variables are optimized out, breakpoints shift, and the call stack may be inaccurate. <span class="warn">Correct firmware must not depend on side effects of undefined behavior or non-`volatile` MMIO access.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
