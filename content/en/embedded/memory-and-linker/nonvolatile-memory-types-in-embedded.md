---
id: emb-memlink-0010
title: "What types of non-volatile memory are used in embedded systems?"
description: "Embedded systems use NOR Flash, NAND Flash, EEPROM, and ROM/OTP, each with different read, write, erase characteristics and typical applications."
track: embedded
section: memory-and-linker
level: junior
type: comparison
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

**NOR Flash** – byte-level reading, XIP (execute-in-place), addressable bus; used for firmware storage (MCU built-in Flash).[2] Slow block erase (~10K cycles).

**NAND Flash** – high density, cheaper; page-level reading only, not XIP.[2] SD cards, eMMC, SSDs; requires FTL (flash translation layer).

**EEPROM** – byte-level erase/write, ~1M cycles; slow, small capacity; for configuration and settings.

**ROM / OTP** – written once or at manufacturing; bootloader in some MCUs.[^dou-embedded-interview]

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
