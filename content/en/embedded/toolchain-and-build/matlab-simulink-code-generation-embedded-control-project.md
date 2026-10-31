---
id: emb-build-0026
title: "When is a model in MATLAB/Simulink or code generation appropriate in an embedded control project?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-optimize-options
    title: "GCC manual: Options That Control Optimization"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
---

## Short answer

A model is appropriate for control algorithms, plant simulation, fixed-point analysis, auto-generated code, and requirements traceability. It is useful when the team validates behavior before hardware exists or must meet safety/process requirements. <span class="warn">Generated code must still be reviewed like firmware: timing, memory, toolchain settings, MISRA rules, and target integration.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
