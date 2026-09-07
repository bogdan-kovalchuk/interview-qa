---
id: emb-fnptr-0025
title: "Trap: why can you not cast any address to a function pointer and call it?"
description: "The address may not be a valid entry point for a function with the required ABI signature."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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

<span class="warn">The address may not be a valid entry address for a function with the required ABI signature.</span>

On Cortex-M function addresses carry Thumb-state bit semantics; calling a wrong address can cause a HardFault. The address may also point to data memory, padding, a bootloader table or a function with a different calling convention.

Protection: call only valid function entry points with the correct signature. For a bootloader jump use the documented sequence: deinit, set MSP, set VTOR, jump to Reset_Handler.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
