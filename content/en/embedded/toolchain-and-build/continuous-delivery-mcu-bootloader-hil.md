---
id: emb-build-0025
title: "How can you provide Continuous Delivery for an MCU device with a physical target, bootloader, and hardware-in-the-loop tests?"
description: "The CD pipeline builds signed artifacts, flashes via bootloader or debug probe, runs HIL tests, and uses managed rigs with power cycling, logs, reset control, and version readback."
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

The CD pipeline must build signed artifacts, flash the device through the bootloader/debug probe, run smoke/HIL tests, and collect logs/trace. Managed test rigs are needed: power cycling, serial logs, reset control, version readback, and failure recovery. The **release gate** must verify not only the build but also the update path, rollback, and basic hardware operation.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
