---
id: emb-build-0020
title: "How do you manage C/C++ firmware dependencies without accidentally pulling in non-portable or heap-heavy code?"
description: "Pin dependency versions, check licenses, toolchain support, heap and RTTI usage, and map-file footprint; prefer small known libraries over generic packages."
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

Pin dependency versions, check licenses, supported toolchains, heap/RTTI/exceptions usage, and footprint in the map file. It is better to add small libraries with known configuration than to pull in a generic package with hidden POSIX, filesystem, or allocation assumptions. **Dependency review** for an MCU must include RAM/flash cost and behavior in ISR/RTOS context.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
