---
id: emb-build-0022
title: "How do you configure CI to build firmware for multiple target platforms and toolchains?"
description: "CI uses a target x toolchain x config matrix; each job installs a pinned toolchain, builds, runs analysis and tests, and collects ELF, HEX/BIN, map, and log artifacts."
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

CI uses a **target x toolchain x config** matrix: for example GCC/Clang, debug/release, board variants. Each job installs a pinned toolchain, runs configure/build, static analysis, and unit tests, then collects artifacts: ELF, HEX/BIN, map, and logs. For target-only checks, HIL runners or nightly hardware jobs are attached separately.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
