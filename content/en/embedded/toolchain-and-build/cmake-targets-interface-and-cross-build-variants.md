---
id: emb-build-0021
title: "How can CMake describe dependencies, targets, interface include directories, and cross-platform build variants?"
description: "In CMake every library or application is a target with its own sources, definitions, include dirs, and link dependencies; INTERFACE vs PRIVATE controls header visibility."
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

In CMake, every library/application must be a **target** with its own sources, compile definitions, include dirs, and link dependencies. `target_include_directories(... INTERFACE)` publishes headers to consumers, while `PRIVATE` keeps them local. Cross-build variants are set via a toolchain file, presets, target-specific options, and separate targets for the MCU, host tests, and utilities.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
