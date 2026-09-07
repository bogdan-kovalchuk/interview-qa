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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**It is a table of handler function addresses** that the CPU uses on exception/interrupt entry.

On Cortex-M the vector table starts with the stack pointer value, followed by the addresses of Reset_Handler, NMI_Handler, HardFault_Handler and IRQ handlers. It is not a regular C callback API, but conceptually it is a table of function entry addresses.

Rule: the ISR handler signature and placement in the vector table must match the startup code, linker script and platform ABI.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
