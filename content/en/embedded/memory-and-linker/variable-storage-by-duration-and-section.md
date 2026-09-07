---
id: emb-memlink-0009
title: "Where can a variable be stored?"
description: "A variable may reside on the stack, heap, or static storage depending on storage duration, with typical sections .data, .bss, .rodata, and .text."
track: embedded
section: memory-and-linker
level: junior
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

A variable can reside in different places depending on storage duration and the linker script. Local automatic variables typically live on the **stack**, dynamic objects from `malloc` on the **heap**, globals and `static` in static storage.[^dou-embedded-interview]

Typical sections: `.data` – initialized global/static variables, copied from Flash to RAM; `.bss` – zeroed or uninitialized global/static, zeroed by startup code; `.rodata` – constants; `.text` – machine code. The compiler may also hold values in registers temporarily.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
