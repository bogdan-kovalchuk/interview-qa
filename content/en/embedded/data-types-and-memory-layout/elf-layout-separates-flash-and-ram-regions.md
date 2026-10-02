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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: gnu-ld-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes LMA/VMA and example runtime copying; the target linker script determines actual placement."
  - source_id: gnu-ld-script
    title: "GNU ld: Linker Scripts"
    url: https://www.sourceware.org/binutils/docs/ld/Scripts.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains the linker's role in mapping sections and laying out output; it does not define a universal ELF layout."
---

## Short answer

**Typical Flash**: `[.text][.rodata][.data LMA]`
**Typical RAM**: `[.data VMA][.bss][heap]...[stack]`

LMA (Load Memory Address) is where bytes are loaded from; VMA (Virtual Memory Address) is a section's run-time address. For `.data`, they often refer to Flash and RAM respectively, and startup code copies the data between them.

Check: `arm-none-eabi-objdump -h firmware.elf` or `arm-none-eabi-size firmware.elf`[^gnu-ld-lma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
