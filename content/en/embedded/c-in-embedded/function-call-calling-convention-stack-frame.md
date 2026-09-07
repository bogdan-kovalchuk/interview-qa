---
id: emb-cemb-0011
title: "How does a function call work?"
description: "A function call follows the calling convention of the ABI: arguments go in registers or on the stack, and the function builds a stack frame for locals."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

During a function call, the compiler follows the **calling convention** of the specific ABI.[^dou-embedded-interview] Arguments are passed in registers or on the stack, the return address is saved, control transfers to the function code, and the function creates its own **stack frame** for local variables and saved registers.

After execution, the result is returned usually in a register or through a hidden pointer for large structs. The needed registers and the stack pointer are then restored, and a return is performed to the call address. Details differ between x86-64, ARM Cortex-M, AAPCS, and others, but the idea is the same: an agreed contract between caller and callee.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
