---
id: emb-memlink-0007
title: "What types of memory segments do you know?"
description: "A C program is laid out in .text, .rodata, .data, .bss, stack, and heap segments, each with a distinct purpose and firmware placement."
track: embedded
section: memory-and-linker
level: junior
type: concept
tags: []
status: published
updated: 2026-09-13
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

Typical memory layout of a C program:[^dou-embedded-interview]

- **.text** – machine code. Read-only, and on MCUs usually in Flash.
- **.rodata** – read-only data: string literals and some constants.
- **.data** – globals and statics with non-zero initialization, copied from Flash to RAM at startup.
- **.bss** – globals and statics with no initialization or `= 0`, zeroed by startup code;
- **Stack** – locals, arguments, return addresses;
- **Heap** – dynamic memory (`malloc`). On most architectures the stack grows down and the heap up, but that is platform/ABI dependent, not a rule of the C standard.
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
