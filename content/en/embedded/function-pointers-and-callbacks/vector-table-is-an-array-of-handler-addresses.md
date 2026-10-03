---
id: emb-fnptr-0023
title: "What is the interrupt vector table in terms of function pointers?"
description: "It is a table of handler function addresses that the CPU uses on exception or interrupt entry."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Cortex-M4 example: the vector table contains the initial stack pointer and reset/exception handler addresses; other cores and MCUs may differ."
---

## Short answer

**It is an architecture-defined table of vectors**, including handler addresses used on exception/interrupt entry.

On Cortex-M the first entry provides the initial stack pointer, and subsequent entries contain addresses such as Reset_Handler. This is not a regular C callback API: the layout is defined by the architecture, startup code and linker configuration.[^arm-cortex-m-startup]

The ISR handler signature and vector table placement must match the startup code, linker script and platform ABI.[^arm-cortex-m-startup]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
