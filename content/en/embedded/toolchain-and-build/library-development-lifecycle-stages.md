---
id: emb-build-0006
title: "Describe the stages of developing a library or program."
description: "The typical development cycle is requirements, API design, implementation, tests, integration, documentation, release, and maintenance, with upfront attention to the public API and version compatibility."
track: embedded
section: toolchain-and-build
level: junior
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

Typical cycle: requirements, API/architecture design, implementation, tests, integration, documentation, release, and maintenance.[^dou-embedded-interview] For a library it is especially important to define the public API, invariants, errors, dependencies, and version compatibility upfront.

In practice this means: write headers and function contracts, implement modules, add unit tests and usage examples, check edge cases, set up build/CI, document limitations. In embedded, memory checks, execution time, interrupt-safety, and behavior on target hardware are also added.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
