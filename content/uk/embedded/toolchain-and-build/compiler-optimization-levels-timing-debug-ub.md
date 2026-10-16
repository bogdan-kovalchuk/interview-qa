---
id: emb-build-0018
title: "Як compiler optimization levels впливають на timing, debug і undefined behavior у firmware?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Вищі `-O` рівні змінюють instruction order, inline, register allocation і timing, тому delay loops, race conditions і UB можуть проявитися інакше. Debug стає складнішим: змінні optimized out, breakpoints зсуваються, call stack може бути неточним. <span class="warn">Коректний firmware не повинен залежати від побічних ефектів UB або не-`volatile` доступу до MMIO.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
