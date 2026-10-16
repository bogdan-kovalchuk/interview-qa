---
id: emb-build-0017
title: "What is cross-compilation, and what common mistakes occur when running a binary on another architecture?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Cross-compilation is building on a host machine for a different CPU/OS/ABI target. Common mistakes: building for the host, mixing up the sysroot, soft/hard-float ABI, endianness, or libc, then getting an `Exec format error` or a runtime crash. Verification requires `file`, `readelf -h`, the target triplet, and toolchain flags.[^dou-embedded-interview]

## Detailed explanation

TODO
