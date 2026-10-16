---
id: emb-build-0019
title: "Які типи optimization використовує компілятор і як перевірити, що оптимізація не зламала MMIO або delay loop?"
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

Компілятор робить inlining, dead-code elimination, constant propagation, loop optimization, instruction scheduling і LTO. MMIO перевіряй через `volatile` register definitions, barriers там, де потрібен порядок, disassembly/map review і target tests. <span class="warn">Busy delay loop без `volatile`, timer або intrinsic barrier може бути скорочений чи прибраний оптимізатором.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
