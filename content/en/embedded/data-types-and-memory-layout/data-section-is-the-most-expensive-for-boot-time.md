---
id: emb-dtypes-0062
title: "Which data does startup code typically copy from Flash to RAM before `main()`?"
description: "Startup code commonly copies the initial contents of `.data` from Flash to RAM before main()."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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
    applicability: "Describes LMA/VMA and example runtime copying of data and clearing bss; exact initialization is platform-specific."
---

## Short answer

Startup code commonly copies `.data` initial bytes from Flash to RAM before `main()` when the section has distinct load and run addresses. The time depends on section size and memory behavior, so `.data` is not universally the most expensive part of startup.[^gnu-ld-lma]

`.bss` is often cleared in RAM, while placement of `.text`, `.rodata`, and other sections is defined by the linker script and platform.[^gnu-ld-lma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
