---
id: emb-dtypes-0040
title: "What does `sizeof(void*)` return on a 32-bit versus a 64-bit platform?"
description: "A pointer's size is set by the address space's width, not by the type it points to."
track: embedded
section: data-types-and-memory-layout
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

32-bit (Cortex-M): `sizeof(void*) = 4` bytes.
64-bit (x86-64, Cortex-A): `sizeof(void*) = 8` bytes.

A pointer's size is determined by the **width of the address space**, NOT by the type it points to: `sizeof(char*) == sizeof(int*) == sizeof(void*)` on the same platform.

Check: `sizeof(void*)`. Do not rely on a specific value in portable code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
