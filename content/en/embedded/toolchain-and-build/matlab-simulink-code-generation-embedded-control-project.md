---
id: emb-build-0026
title: "When is a MATLAB/Simulink model or code generation appropriate in an embedded control project?"
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

A model is appropriate for control algorithms, plant simulation, fixed-point analysis, auto-generated code, and requirements traceability. It is useful when the team validates behavior before hardware or has safety/process requirements. <span class="warn">Generated code still needs to be reviewed as firmware: timing, memory, toolchain settings, MISRA rules, and target integration.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
