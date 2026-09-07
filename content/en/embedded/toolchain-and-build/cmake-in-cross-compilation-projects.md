---
id: emb-build-0009
title: "How does CMake work in a cross-compilation project for an MCU or Embedded Linux?"
description: "CMake configures the build graph from CMakeLists.txt and a toolchain file, then the build tool invokes the cross-compiler, assembler, linker, and post-build utilities."
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

CMake first configures the build graph: it reads `CMakeLists.txt`, the toolchain file, target flags, and generates a Ninja/Make project. Then the build tool invokes the cross-compiler, assembler, linker, and post-build utilities such as `objcopy`. It is important to separate host tools, which run on the PC, from target binaries, which are intended for the MCU or Linux target.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
