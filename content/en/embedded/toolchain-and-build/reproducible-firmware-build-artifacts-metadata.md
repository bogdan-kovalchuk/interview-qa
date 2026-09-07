---
id: emb-build-0023
title: "How do you organize a reproducible firmware build with a pinned toolchain, artifacts, a map file, and version metadata?"
description: "Pin the toolchain version, build container, CMake presets, and dependency versions; store ELF, HEX/BIN, map, compiler flags, and commit hash in build artifacts."
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

Pin the toolchain version, build container or package hash, CMake presets/options, and dependency versions. Store `.elf`, `.hex`/`.bin`, `.map`, symbol/version info, compiler flags, and commit hash in the artifacts. **Version metadata** in firmware must allow exact reproduction of the binary running on the device.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
