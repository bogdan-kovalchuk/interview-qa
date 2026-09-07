---
id: emb-memlink-0015
title: "What does the linker do, and how does it place .text, .rodata, .data, .bss, stack, and heap?"
description: "The linker resolves symbols and places program sections in Flash and RAM according to the linker script."
track: embedded
section: memory-and-linker
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Linker** resolves symbols/relocations, pulls the needed objects from libraries and places sections into memory regions. Typically `.text`/`.rodata` go into Flash, `.data` has a load image in Flash and a runtime address in RAM, `.bss` is zero-initialized in RAM. Stack/heap boundaries are set by the linker script or startup code, and a mistake here causes a hard fault or corruption.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
