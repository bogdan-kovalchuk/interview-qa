---
id: emb-build-0015
title: "What is a translation unit, and why can include files cause multiple-definition or ODR problems?"
description: "A translation unit is one preprocessed source file with its included headers; non-static definitions in headers cause multiple definitions or ODR violations."
track: embedded
section: toolchain-and-build
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for toolchain and build concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Translation unit** is the result of preprocessing one `.c/.cpp` file together with all included headers. If a header contains a non-static object or function definition, it ends up in every translation unit and the linker sees multiple definitions. In C++ this can also violate the ODR; headers should contain only declarations, `inline`/`constexpr`, or templates as the language rules allow.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
