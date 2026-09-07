---
id: emb-build-0024
title: "How do you build an MCU project build system with a bootloader, application, tests, and hardware variants?"
description: "Split the build into separate targets for bootloader, app, shared drivers, host tests, target tests, and board configs, each with its own linker script and memory layout."
track: embedded
section: toolchain-and-build
level: senior
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

Split the build into separate targets: `bootloader`, `app`, shared drivers, host tests, target tests, and board configs. Each target has its own linker script, startup file, compile definitions, memory layout, and output artifacts. Hardware variants are better described through board files/config targets rather than conditional blocks in every source file.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
