---
id: emb-build-0012
title: "How can you obtain preprocessing, assembly, and object files during compilation?"
description: "GCC/Clang flags -E, -S, and -c produce preprocessed output, assembly, and object files, and tools like objdump and readelf help analyze firmware."
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

For GCC/Clang: `-E` produces preprocessed output, `-S` – assembly, `-c` – object file without linking. For firmware analysis, `objdump -d`, `readelf -S`, and the linker map are useful. In CMake, these flags can be temporarily added to a target or the compiler command can be run from `compile_commands.json`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
