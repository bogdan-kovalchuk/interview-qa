---
id: emb-build-0017
title: "What is cross-compilation, and what common mistakes occur when running a binary on another architecture?"
description: "Cross-compilation builds on a host for a different CPU, OS, or ABI; common mistakes include wrong sysroot, mixed ABI or endianness, and host-target confusion."
track: embedded
section: toolchain-and-build
level: middle
type: pitfall
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

Cross-compilation is building on a host machine for a different CPU/OS/ABI target. Common mistakes: building for the host, mixing up the sysroot, soft/hard-float ABI, endianness, or libc, then getting an `Exec format error` or a runtime crash. Verification requires `file`, `readelf -h`, the target triplet, and toolchain flags.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
