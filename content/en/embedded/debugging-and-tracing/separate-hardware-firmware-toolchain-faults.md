---
id: emb-debug-0002
title: "How do you distinguish a hardware fault, firmware bug, and toolchain or configuration issue while debugging a board?"
description: "First check power, clocks, reset, boot pins, and signal levels with an oscilloscope or logic analyzer."
track: embedded
section: debugging-and-tracing
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for debugging and tracing concepts; details of specific devices and toolchains can differ."
---

## Short answer

First check power, clocks, reset, boot pins, and signal levels with an oscilloscope or logic analyzer. Then minimize the firmware to a known-good test: blink, UART, single peripheral, no RTOS/DMA. If the symptom depends on optimization, linker script, startup, or wrong flags, it looks like toolchain/config; if it repeats with minimal code and is visible on signals, it is a hardware/power issue.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
