---
id: emb-fnptr-0024
title: "How do you declare an ISR handler type with no arguments and no return value?"
description: "A function-pointer type describes a C callback with no arguments and no return value, but not the hardware vector table format."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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
    applicability: "Cortex-M4 example: the vector table has an initial stack pointer and handler addresses; it is not a homogeneous C function-pointer array."
---

## Short answer

Typically:

`typedef void (*isr_handler_t)(void);`

This typedef declares a C function pointer type, but does not by itself describe a hardware vector table. On Cortex-M the first vector is the initial stack pointer, so the table has a special layout.[^arm-cortex-m-startup]

Do not declare the entire Cortex-M vector table as a homogeneous array of `isr_handler_t`; startup code and the linker script define its platform-specific format.[^arm-cortex-m-startup]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
