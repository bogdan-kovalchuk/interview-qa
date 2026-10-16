---
id: emb-build-0026
title: "Коли модель у MATLAB/Simulink або code generation доречна в embedded control project?"
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

Модель доречна для control algorithms, plant simulation, fixed-point analysis, auto-generated code і requirements traceability. Вона корисна, коли команда валідує поведінку до hardware або має safety/process requirements. <span class="warn">Generated code все одно треба review-ити як firmware: timing, memory, toolchain settings, MISRA rules і target integration.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
