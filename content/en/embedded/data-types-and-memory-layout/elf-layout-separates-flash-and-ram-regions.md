---
id: emb-dtypes-0065
title: "What does a typical section layout look like in a Cortex-M `.elf` file?"
description: "Flash holds .text, .rodata, and the .data LMA; RAM holds the .data VMA, .bss, the heap, and the stack."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Flash (ROM)**: `[.text][.rodata][.data LMA]`
**RAM**: `[.data VMA][.bss][heap ↑]...[stack ↓]`

LMA (Load Memory Address) is where bytes are stored in Flash. VMA (Virtual Memory Address) is where the CPU expects them in RAM. Startup code copies LMA -> VMA for `.data`.

Check: `arm-none-eabi-objdump -h firmware.elf` or `arm-none-eabi-size firmware.elf`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
